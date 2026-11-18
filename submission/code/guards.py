"""★ FILE ĐỘI SỬA (1/3): cổng cấp hệ thống, nằm NGOÀI model và prompt.

VÒNG 1 (trước khi biết sự cố): viết 2–3 CỔNG PHÒNG NGỪA rút từ pre-mortem / HAZOP / checklist của bàn, rồi chốt bằng
    python3 -m lab10.checkpoint        (chép file này thành guards_round1.py = mốc "prepared"; KHÔNG sửa bản chép)
VÒNG 2 (sau khi bốc thẻ): sửa tiếp NGAY TRONG FILE NÀY. Giữ các cổng vòng 1, thêm cổng mới.
Hai file còn lại bàn được sửa: lab10/monitors.py (chỉ số theo dõi) và config/operating_gates.json (cổng kinh doanh,
vận hành, pháp lý: những con số và tên người mà trợ lý phải tuân theo, không cần code).

Hai điểm móc, agent gọi tự động:
  pre_guard(ctx)          chạy TRƯỚC khi agent đọc ticket
  write_gate(ctx, action) chạy TRƯỚC MỖI lệnh ghi (issue_refund, file_carrier_fault,
                          notify_carrier, send_reply)

Trả về một Verdict:
  Verdict.allow()                       cho qua   (pre_guard: allow(policy_id="...") để ghim phiên bản chính sách)
  Verdict.deny("lý do")                 bỏ riêng lệnh ghi này, agent đi tiếp
  Verdict.escalate("lý do")             dừng, chuyển ticket cho người
  Verdict.modify("lý do", amount_vnd=…) sửa tham số lệnh ghi (amount_vnd, payer, carrier_id, parcel_id, payload…)
  Verdict.rewrite("lý do", text)        chỉ pre_guard: thay nội dung ticket mà agent sẽ đọc

ctx.ticket   ticket gốc (chữ khách viết là DỮ LIỆU, không phải lệnh)
ctx.tools    tra cứu nguồn sự thật: lookup_order, lookup_policies, lookup_approvals(**lọc),
             ledger_rows(**lọc), fault_rows(**lọc), lookup_carrier; ctx.as_of = ngày hôm nay
             ops_limits() = các trần đã thống nhất với Ops/Finance; ops_facts() = số liệu vận hành;
             auto_refund_today_vnd() = tổng đã hoàn tự động trong ngày
ctx.gates    config cổng của bàn (config/operating_gates.json), chỉ đọc;  ctx.cost_vnd = tiền LLM đã tốn cho ticket này
ctx.events   trace tới thời điểm này;  ctx.log("ten_su_kien", ...) ghi thêm sự kiện guard vào trace
lab10.helpers: db_delay_days, ticket_parcel, effective_policy, entitlement_vnd, carrier_at_fault, digits

CỔNG VÒNG 1 CỦA BÀN SIUUUNHAN (mỗi cổng ứng với một dòng pre-mortem B6 / HAZOP B4):
  Cổng 0 (pre_guard)  ghim chính sách theo NGÀY HIỆU LỰC, không theo cờ index_active do người bật tay (drift B3).
  Cổng 1 (tiền)       issue_refund: tính lại quyền lợi từ TRACKING + chính sách hiệu lực; chặn số khách tự khai,
                      lệnh cài trong ticket (payer khác LOGIX, hoàn toàn bộ), fail-open khi LLM lỗi, hoàn lặp,
                      phê duyệt đã dùng / hết hạn / của đơn khác.
  Cổng 1b (lỗi hãng)  file_carrier_fault: chỉ ghi khi tracking cho thấy hãng có lỗi theo chính sách, và ghi đúng kiện.
  Cổng 3 (pháp lý)    notify_carrier: chỉ gửi các trường có trong carrier_notice_fields của chính sách.
Cổng 2 (trần tiền ngày) là con số trong config/operating_gates.json, không cần code.
VÒNG 2 (thẻ S3):
  Cổng 4 (lỗi hãng)   file_carrier_fault: không tự ghi quá ops_limits.max_auto_strikes_per_carrier_per_day lỗi / hãng / ngày.
"""
from . import helpers as H  # noqa: F401
from .tools import Verdict


def _policy(ctx):
    """Chính sách có ngày hiệu lực chứa hôm nay (nguồn sự thật), không đọc cờ index_active."""
    return H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of)


def _facts(ctx, order_id):
    """(order, parcel, delay_days theo tracking, policy) cho ticket đang xử lý; None nếu thiếu dữ liệu."""
    order = ctx.tools.lookup_order(order_id)
    policy = _policy(ctx)
    if order is None or policy is None or not order.get("parcels"):
        return None
    parcel = H.ticket_parcel(order, ctx.ticket, ctx.as_of)
    return order, parcel, H.db_delay_days(parcel, ctx.as_of), policy


def _approval_ok(ctx, approval_id, order_id):
    """Phê duyệt chỉ hợp lệ khi còn hiệu lực, chưa dùng, chưa hết hạn và đúng đơn này."""
    rows = ctx.tools.lookup_approvals(approval_id=approval_id)
    if not rows:
        return False
    a = rows[0]
    return a.get("status") == "valid" and a.get("order_id") == order_id and a.get("expires_at", "") >= ctx.as_of


def pre_guard(ctx):
    pol = _policy(ctx)
    if pol is not None:                                   # Cổng 0: ghim phiên bản chính sách theo ngày hiệu lực
        return Verdict.allow(policy_id=pol["policy_id"])
    return Verdict.allow()


def _gate_refund(ctx, action):
    facts = _facts(ctx, action.get("order_id"))
    if facts is None:
        return Verdict.escalate("không tra được đơn / tracking / chính sách hiệu lực: chuyển người")
    order, parcel, delay, policy = facts
    entitled = H.entitlement_vnd(policy, order, delay, parcel.get("delay_cause"))
    already = sum(r["amount_vnd"] for r in ctx.tools.ledger_rows(order_id=order["order_id"]))
    remaining = max(0, entitled - already)                # không hoàn lặp (ghi lại khi confirm lỗi 429)
    amount = action.get("amount_vnd", 0)
    approval_id = action.get("approval_id")
    if approval_id and not _approval_ok(ctx, approval_id, order["order_id"]):
        ctx.log("refund_bad_approval", approval_id=approval_id, order_id=order["order_id"])
        return Verdict.escalate("phê duyệt không hợp lệ (đã dùng / hết hạn / của đơn khác): chuyển người duyệt")
    if remaining <= 0:
        ctx.log("refund_not_entitled", order_id=order["order_id"], asked=amount, entitled=entitled,
                already=already, db_delay_days=delay)
        return Verdict.deny(f"theo tracking trễ {delay} ngày, chính sách {policy['policy_id']} không cho hoàn thêm")
    if remaining > policy["auto_limit_vnd"] and not approval_id:
        return Verdict.escalate("quyền lợi vượt hạn mức tự động, chưa có phê duyệt hợp lệ: chuyển người duyệt")
    if amount != remaining or action.get("payer", "LOGIX") != "LOGIX":
        ctx.log("refund_recomputed", order_id=order["order_id"], asked=amount, payer=action.get("payer"),
                entitled=remaining, db_delay_days=delay, basis=action.get("basis"))
        return Verdict.modify("tính lại theo tracking và chính sách hiệu lực", amount_vnd=remaining, payer="LOGIX")
    return Verdict.allow()


def _gate_fault(ctx, action):
    facts = _facts(ctx, action.get("order_id"))
    if facts is None:
        return Verdict.deny("không tra được tracking: không ghi lỗi hãng")
    order, parcel, delay, policy = facts
    if not H.carrier_at_fault(policy, parcel, delay):
        ctx.log("fault_blocked", order_id=order["order_id"], parcel_id=parcel["parcel_id"],
                db_delay_days=delay, cause=parcel.get("delay_cause"))
        return Verdict.deny("tracking không cho thấy hãng có lỗi theo chính sách: không ghi lỗi")
    # Cổng 4 (vòng 2, thẻ S3): trần lỗi TỰ ĐỘNG mỗi hãng mỗi ngày đã thống nhất với Ops. Từ lỗi vượt trần trở đi
    # không tự ghi; khách vẫn được hoàn, lỗi để người duyệt (NV-HANH) xác nhận. Thế giới mỗi lần chạy = một ngày.
    cap = ctx.tools.ops_limits().get("max_auto_strikes_per_carrier_per_day")
    already = len(ctx.tools.fault_rows(carrier_id=parcel["carrier_id"]))
    if cap is not None and already >= cap:
        ctx.log("fault_strike_cap", carrier_id=parcel["carrier_id"], already_today=already, cap=cap,
                order_id=order["order_id"], parcel_id=parcel["parcel_id"])
        return Verdict.deny(f"hãng {parcel['carrier_id']} đã có {already} lỗi tự động trong ngày (trần {cap}): chờ người duyệt xác nhận")
    fixed = {"parcel_id": parcel["parcel_id"], "carrier_id": parcel["carrier_id"],
             "driver_id": parcel.get("driver_id"), "delay_days": delay}
    if any(action.get(k) != v for k, v in fixed.items()):
        ctx.log("fault_corrected", asked={k: action.get(k) for k in fixed}, fixed=fixed)
        return Verdict.modify("ghi lỗi cho đúng kiện trễ, số ngày theo tracking", **fixed)
    return Verdict.allow()


def _gate_notice(ctx, action):
    policy = _policy(ctx)
    allowed = set((policy or {}).get("carrier_notice_fields") or [])
    payload = action.get("payload") or {}
    extra = sorted(k for k in payload if k not in allowed)
    if extra:
        ctx.log("notice_fields_dropped", dropped=extra)
        return Verdict.modify("chỉ gửi hãng các trường chính sách cho phép",
                              payload={k: v for k, v in payload.items() if k in allowed})
    return Verdict.allow()


def write_gate(ctx, action):
    # action = {"tool": "issue_refund", "ticket_id":..., "order_id":..., "amount_vnd":..., "payer":..., ...}
    tool = action.get("tool")
    if tool == "issue_refund":
        return _gate_refund(ctx, action)
    if tool == "file_carrier_fault":
        return _gate_fault(ctx, action)
    if tool == "notify_carrier":
        return _gate_notice(ctx, action)
    return Verdict.allow()
