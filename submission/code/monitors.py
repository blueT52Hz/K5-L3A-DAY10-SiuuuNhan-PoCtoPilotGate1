"""★ FILE ĐỘI SỬA (2/3): chỉ số theo dõi (monitor). Thêm ÍT NHẤT MỘT chỉ số bắt được sự cố của bàn.

Mỗi monitor nhận danh sách trial (KHÔNG có nhãn đúng/sai, giống production) và trả về một số.
Một trial = {"ticket_id", "seed", "day", "status", "amount_vnd", "ticket", "events", "ledger", "faults", "outbound",
             "arrive_min", "warehouse", "cost_vnd", "review_kind", "queue_wait_min", "queue_stuck"}
  "day"            một ngày vận hành giả lập: các ticket cùng "day" và cùng "seed" chạy nối nhau trên cùng một sổ cái
  "arrive_min"     phút ticket tới trong ca (0..480)          "warehouse"   kho của đơn
  "cost_vnd"       tiền LLM + nền tảng đã tốn cho ticket      "review_kind" None / "escalated" (trợ lý chuyển người) /
  "queue_wait_min" số phút chờ người duyệt (None nếu không vào hàng chờ)     "recheck" (nhân viên tự kiểm lại)
Chỉ số có thể là kỹ thuật (tỉ lệ model đè số trong ticket lên DB), vận hành (số ca cần người trong giờ đông nhất),
hay kinh doanh (tỉ lệ ticket trợ lý đọc xong vẫn phải chuyển người).

lab10.grade kiểm: monitor chạy không lỗi, và giá trị trên gói sự cố khác giá trị trên bộ nền,
tức là monitor "sáng đèn" khi sự cố xảy ra.
"""


def escalation_rate(trials):
    return sum(t["status"] == "escalated" for t in trials) / max(1, len(trials))


def max_auto_faults_per_carrier_day(trials):
    """Số lỗi tự động lớn nhất mà MỘT hãng nhận trong MỘT ngày (nhóm theo day + seed + hãng).

    Đọc sự kiện ghi lỗi hãng trong trace, không cần nhãn. Vượt ops_limits.max_auto_strikes_per_carrier_per_day (= 2)
    nghĩa là hãng đang bị phạt dồn mà không ai xác nhận (thẻ S3). Bình thường: ≤ 1-2."""
    count = {}
    for t in trials:
        for e in t.get("events") or []:
            if e.get("type") == "tool" and e.get("tool") == "file_carrier_fault":
                key = (t.get("day"), t.get("seed"), e.get("carrier_id"))
                count[key] = count.get(key, 0) + 1
    return max(count.values(), default=0)


def fault_gate_block_rate(trials):
    """Tỉ lệ lần chạy mà cổng phải chặn / sửa một lệnh ghi lỗi hãng (sự kiện guard fault_blocked, fault_strike_cap,
    fault_corrected). Tăng đột biến = dữ liệu tracking / chính sách / lượng lỗi theo hãng đang lệch khỏi thường ngày,
    dù cổng đã chặn kịp (phát hiện drift kiểu thẻ S3 trước khi hãng khiếu nại)."""
    kinds = {"fault_blocked", "fault_strike_cap", "fault_corrected"}
    hit = sum(any(e.get("type") == "guard" and e.get("kind") in kinds for e in (t.get("events") or []))
              for t in trials)
    return hit / max(1, len(trials))


MONITORS = {
    "escalation_rate": escalation_rate,     # có sẵn; KHÔNG tính là metric mới của đội
    "max_auto_faults_per_carrier_day": max_auto_faults_per_carrier_day,   # bàn SiuuuNhan, vòng 2 (thẻ S3)
    "fault_gate_block_rate": fault_gate_block_rate,                       # bàn SiuuuNhan, vòng 2 (thẻ S3)
}
STARTER_MONITORS = ("escalation_rate",)
