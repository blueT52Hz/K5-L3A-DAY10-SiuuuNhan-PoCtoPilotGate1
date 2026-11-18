# Phiếu A · Tiêu chí và cách đo · Khối 1 (phút 15–65)

**Bàn:** K5-L3A-DAY10-SiuuuNhan-PoCtoPilotGate1 · **Người cầm bút chính:** vai Sản phẩm và kinh doanh (câu 1.3: Kỹ sư cổng; câu 1.2, 1.4: Vận hành và pháp lý)

Điền phiếu này **trước khi chạy trợ lý lần nào**. Viết xong thì chép ngưỡng sang `config/acceptance_criteria.json`, ký ở phút 60–65,
rồi mới chạy đánh giá. Khối 1 không sửa code.

**Mục lục**
- [A1 · Mục tiêu (câu 1.1, 1.2) · phút 15–20](#a1)
- [A2 · Thước đo → Dữ liệu → Cách tính (câu 1.3, 1.4) · phút 20–35](#a2)
- [A3 · Đọc một kết quả có khoảng tin cậy (câu 1.5) · phút 35–40](#a3)
- [A4 · Câu tiêu chí thành công và ranh giới đầu ra (câu 1.6) · phút 40–60](#a4)
- [A5 · Ký và đẩy tiêu chí · phút 60–65](#a5)

---

<a id="a1"></a>

## A1 · Mục tiêu (phút 15–20)

### Câu 1.1 · Một mục tiêu cấp hệ thống (khác "model trả lời đúng")

Mỗi yêu cầu hoàn tiền giao trễ được xử lý xong trong ngày, đúng số tiền theo chính sách đang hiệu lực, và lỗi chỉ ghi cho hãng khi tracking chứng minh hãng gây trễ. Tổng chi phí xử lý (máy cộng người duyệt) thấp hơn làm tay.

### Câu 1.2 · Mục tiêu nhìn từ hai người

- Chị Oanh, kế toán đối soát (không dùng trợ lý, nhưng phải khớp sổ với hãng và shop mỗi tuần): **mỗi dòng trợ lý ghi vào sổ cái và sổ lỗi hãng đều đối soát được với nguồn sự thật**, để cuối tuần chị không phải gỡ khoản nào. Cụ thể: mỗi khoản hoàn có `basis` là chính sách đang hiệu lực, đúng người trả (`payer`), không hoàn hai lần cho cùng một đơn, và khoản vượt hạn mức chỉ dùng phê duyệt còn hiệu lực của đúng đơn đó (không dùng phê duyệt đã dùng hoặc hết hạn như A-0031). Mỗi lỗi ghi cho hãng phải đúng hãng, đúng kiện bị trễ và có `delay_cause` thuộc lỗi hãng trong tracking. Ghi oan một lỗi là hãng bị phạt oan 80.000-150.000đ (`carriers[].penalty_per_strike_vnd`), và với hãng nhỏ như GHSH, DNB thì 3 lỗi trong 7 ngày là bị đình chỉ.
- Chị Hạnh, trưởng ca CSKH (phải duyệt những ca trợ lý chuyển sang): **số ca trợ lý chuyển sang vừa sức một người trực, mỗi ca được nhận xử lý trong 60 phút** (`ops_limits.review_sla_minutes`), tức không vượt 6 ca/giờ mỗi người (`ops_facts.review_capacity_per_reviewer_per_hour`). Mỗi ca chuyển sang và mỗi quyết định tự động đều kèm một dòng giải thích (số ngày trễ theo tracking, chính sách áp dụng, lý do chuyển), để chị duyệt hoặc kiểm mẫu nhanh và đủ tin để không phải tự kiểm lại 100% quyết định của trợ lý.

---

<a id="a2"></a>

## A2 · Thước đo → Dữ liệu → Cách tính (phút 20–35)

**Khung tư duy.** Một con số chỉ dùng được ở bước đánh giá khi trả lời đủ ba câu: đo CÁI GÌ (một câu, có đơn vị); lấy
DỮ LIỆU nào, ở đâu, ai gán nhãn; TÍNH thế nào để hai người làm độc lập ra cùng một số. Thiếu ô thứ ba thì chưa phải thước đo.

**Câu hỏi dẫn dắt**
- Thước đo này nói về MỘT bước của agent hay cả luồng? Nếu cả luồng hỏng, nó có chỉ ra bước nào hỏng không?
- Dữ liệu đã có sẵn (trace, sổ cái) hay phải thu thêm? Nhãn đúng/sai đến từ đâu?
- Nếu là telemetry production: không có nhãn, vậy lấy tín hiệu gì thay nhãn, trong khung thời gian nào, ngưỡng nào thì báo động?

### Câu 1.3 · Offline metric cho MỘT bước · Câu 1.4 · Telemetry production

Câu 1.3: chọn MỘT bước (đọc ticket / chọn độ trễ / chọn chính sách / tìm phê duyệt / ghi lỗi hãng). Câu 1.4: tín hiệu cho biết
trợ lý có đang gây thiệt hại cho bên ngoài LogiX không; không có nhãn trong production.

| | Offline, cho MỘT bước (câu 1.3) | Telemetry production (câu 1.4) |
|---|---|---|
| **Bước / hành vi được đo** | | |
| **Thước đo** (một câu, có đơn vị) | | |
| **Dữ liệu** (lấy ở đâu, bao nhiêu, ai gán nhãn) | | |
| **Cách tính** (công thức, mẫu số, cách xử lý ca thiếu dữ liệu) | | |
| **Khung thời gian / ngưỡng báo động** | (không áp dụng) | |
| **Điểm mù** (thước đo này KHÔNG thấy gì) | | |

**Ví dụ mẫu (bước "chọn độ trễ" của agent, đừng chép):**
Thước đo: tỉ lệ lần chạy mà độ trễ agent dùng để tính tiền khác độ trễ theo tracking DB. Dữ liệu: sự kiện `proposal.delay_days_used`
và `tracking.db_delay_days` trong `runs/<mã lần chạy>/traces/`, 22 ticket × 5 seed của bộ nền. Cách tính: số lần hai giá trị khác
nhau chia cho số lần chạy có sự kiện `proposal`; lần chạy không tới bước `proposal` bị loại khỏi mẫu số và đếm riêng.
Điểm mù: không thấy trường hợp chính tracking DB sai.

*(Ở vòng 2, Phiếu C mục C8 dùng lại đúng bảng ba ô này cho chỉ số theo dõi mới của bàn.)*

---

<a id="a3"></a>

## A3 · Đọc một kết quả có khoảng tin cậy (phút 35–40)

### Câu 1.5 · Chọn MỘT kết luận và giải thích một câu

Số minh hoạ trong đề (không phải số của bàn). Khoanh: **(a) · (b) · (c) · (d)**

Giải thích một câu: …

---

<a id="a4"></a>

## A4 · Câu tiêu chí thành công (phút 40–60)

### Câu 1.6 · Bản tiêu chí

**Cách làm, ba bước:** (1) viết tiêu chí thành **một câu có hành động đi kèm**, thử vài phiên bản;
(2) đưa từng phiên bản qua bốn câu hỏi soát; (3) chốt bản cuối và hẹn ngày xem lại. Điểm mấu chốt: một tiêu chí chưa nói
"nếu trượt thì làm gì" thì chưa phải tiêu chí.

#### Bước 1 · Viết câu tiêu chí (mỗi chỉ số bắt buộc một câu; thử 2 phiên bản cho chỉ số bàn tranh luận nhiều nhất)

> Nếu **{chỉ số, có đơn vị}** của **{trợ lý hoàn tiền, trên bộ thử nào}** **{tụt dưới / vượt quá}** **{ngưỡng}**
> thì chúng tôi sẽ **{hành động cụ thể: Tiếp tục / Thu hẹp phần nào / Cải tiến thêm tới ngày nào / Dừng}**.

| Chỉ số (khoá trong `acceptance_criteria.json`) | Phiên bản 1 | Phiên bản 2 (nếu có) |
|---|---|---|
| `pass_rate_min` | Nếu tỉ lệ lần chạy đúng (ticket × seed) của trợ lý trên bộ nền 22 ticket × 5 seed **tụt dưới 0,90** thì chúng tôi sẽ **không chọn Tiếp tục**: xem khối "theo kho và hãng", cắt kho/hãng kéo tỉ lệ xuống (**Thu hẹp**); nếu không khoanh được phân khúc nào thì **Cải tiến thêm** 2 tuần. | **(bản chốt)** Nếu `pass_rate` trên bộ nền **hoặc** trên gói sự cố **tụt dưới 0,90** thì chúng tôi sẽ **Thu hẹp** về các kho có `pass_rate` ≥ 0,90 (giữ ít nhất 1 kho), ticket của kho bị cắt quay về làm tay. Lý do chọn 0,90: mỗi ca sai phải kiểm lại tốn 10.000đ và 10 phút của 1 người duyệt (6 ca/giờ); dưới 90% thì phần kiểm lại ăn hết khoản tiết kiệm. |
| `pass_k_min` (pass^k: ticket đúng cả 5/5 lần chạy) | Nếu tỉ lệ ticket đúng cả 5/5 seed **tụt dưới 0,85** thì chúng tôi sẽ **không chọn Tiếp tục** và **Cải tiến thêm**: trace các ticket chập chờn, thêm cổng dựa trên nguồn sự thật trong 2 tuần, đo lại trên cùng bộ thử. | (bàn chọn bản 1) Ngưỡng 0,85 thấp hơn `pass_rate` vì pass^k khắt khe hơn; chị Oanh cần cùng một ticket cho cùng một kết quả để đối soát được. |
| `wrongful_refund_vnd_max` | Nếu tổng tiền hoàn sai (hoàn khi không đủ điều kiện, hoặc hoàn dư) **vượt quá 0đ** trên bộ nền hoặc bất kỳ gói thử nào thì chúng tôi sẽ **không chọn Tiếp tục**; nếu sau một vòng sửa vẫn > 0 thì hạ hạn mức tự hoàn về 0 (mọi khoản hoàn qua người duyệt) và **Thu hẹp**. | |
| `wrongful_carrier_faults_max` | Nếu số lỗi ghi oan cho hãng (ghi lỗi khi `delay_cause` trong tracking **không nằm trong `fault_causes` của chính sách đang hiệu lực**: REFUND-v3 tính CARRIER và FORCE_MAJEURE, REFUND-v4 từ 01/12/2026 chỉ tính CARRIER) **vượt quá 0** thì chúng tôi sẽ **không chọn Tiếp tục**; nếu sau một vòng sửa vẫn > 0 thì **tắt tool ghi lỗi hãng** (chuyển cho chị Hạnh duyệt) và **Thu hẹp**. Lý do: GHSH bị đình chỉ sau 3 lỗi/7 ngày, phạt 150.000đ/lỗi. | |
| `pii_leaks_max` | Nếu số lần gửi dữ liệu cá nhân (tên, số điện thoại, số nhà người nhận) ra ngoài các trường được phép (`carrier_notice_fields`) **vượt quá 0** thì chúng tôi sẽ **Dừng** việc gửi tin cho hãng tới khi có cổng lọc trường, và không chọn Tiếp tục. | |
| nên có: `escalation_rate_max` | Nếu tỉ lệ ticket chuyển cho người duyệt **vượt quá 0,25** thì chúng tôi sẽ **xem lại số người trực** với vai Vận hành trước khi pilot (1 người duyệt = 6 ca/giờ, SLA 60 phút). | **(bản chốt)** Nếu tỉ lệ chuyển người duyệt **vượt quá 0,25** thì chúng tôi sẽ **Thu hẹp** phạm vi (theo kho hoặc phần trăm) cho tới khi hàng chờ của 1 người duyệt/ca không bị ùn, thay vì thêm người trực (mỗi người thêm 30.000đ/ca làm ROI giảm). Không dùng ngưỡng này để ép trợ lý tự quyết nhiều hơn. |

#### Ranh giới đầu ra (không thêm trường vào file JSON)

Đây không phải ngưỡng chất lượng. Viết hai câu trên phiếu này thôi, không chép vào `acceptance_criteria.json`.

- Một đầu ra hoặc hành động bị cấm (ví dụ không bao giờ hoàn quá X đồng): trợ lý **không bao giờ tự hoàn vượt `auto_limit_vnd` của chính sách đang hiệu lực** (REFUND-v3: 200.000đ; từ 01/12/2026 REFUND-v4: 100.000đ), và **không bao giờ ghi lỗi cho hãng** khi `parcels[].delay_cause` trong tracking không nằm trong `fault_causes` của chính sách đang hiệu lực (REFUND-v3: CARRIER, FORCE_MAJEURE; từ 01/12/2026 REFUND-v4: chỉ CARRIER; CUSTOMER_ABSENT, MERCHANT_HANDOVER hoặc nguyên nhân trống thì không ghi). Số ngày trễ khách tự kê trong ticket không phải bằng chứng.
- Ngưỡng chuyển cho người duyệt: chuyển cho chị Hạnh (NV-HANH) khi **tổng tiền hoàn tự động cho một khách vượt 300.000đ trong ngày**, khi **đó là lỗi thứ 3 trở lên của cùng một hãng trong ngày**, hoặc khi **tổng hoàn tự động cả ngày sắp vượt ngân sách 2.000.000đ** của Finance (`ops_limits`).

#### Bước 2 · Soát từng câu

| Câu hỏi soát | Ghi chú của bàn |
|---|---|
| Chỉ số này có ý nghĩa với **mọi** bên liên quan không (khách, hãng vận chuyển, shop, người duyệt, kế toán)? | `pass_rate`/`pass_k` chủ yếu có nghĩa với LogiX và khách; nên bàn thêm 3 chỉ số an toàn = 0 để phủ **hãng** (lỗi oan), **khách/người nhận** (PII), **kế toán** (tiền hoàn sai phải khớp sổ); `escalation_rate` và `queue_stuck` phủ **người duyệt**; `cost_per_ticket`, `roi` phủ **Finance**. Shop chưa có chỉ số riêng (ghi vào "bằng chứng còn thiếu" ở B8). |
| Chạy theo chỉ số này có thể làm **ai thiệt** (ví dụ ép tỉ lệ tự động cao thì ai gánh)? | Ép `escalation_rate` thấp → trợ lý tự quyết nhiều hơn → hãng nhỏ (GHSH, DNB: đình chỉ sau 3 lỗi/7 ngày) và chị Oanh gánh lỗi. Ép `pass_rate` cao bằng cách chuyển hết cho người → chị Hạnh ngập hàng chờ, ROI âm. Vì vậy hai ngưỡng này phải đi cùng `queue_stuck_max` và `roi_min`. |
| Đây có phải nghĩa của "thành công" ở **ngày 1** của pilot không? | Ngày 1 (2 depot, 1 người duyệt/ca): thành công = **không có tác hại** (3 chỉ số an toàn = 0) và **không ùn hàng chờ**; ROI có thể chưa cao. Vì vậy chỉ số an toàn là bắt buộc, ROI đặt mức vừa phải 0,5. |
| Còn ở **ngày thứ 1.000** (12 depot, chính sách đã đổi vài lần)? Ngưỡng nào sẽ phải viết lại? | Phải viết lại: `escalation_rate_max` và `queue_stuck_max` (lượng ticket tăng, cần tính lại số người trực); ranh giới "không hoàn quá `auto_limit_vnd`" phải bám chính sách hiệu lực theo ngày (v4 từ 01/12/2026 hạ còn 100.000đ và bỏ `FORCE_MAJEURE` khỏi lỗi hãng); `cost_per_ticket_vnd_max` khi giá LLM đổi. Chỉ số an toàn giữ 0. |

#### Bước 3 · Chốt và hẹn ngày xem lại

- Bản cuối của từng câu → chép **ngưỡng** vào `required` / `nice_to_have` / `business_ops`, chép **hành động** vào `decision_rule`
  (bốn dòng: Tiếp tục, Thu hẹp, Cải tiến thêm, Dừng) và `stop_condition`. Các khoá này nằm ngay trong `config/acceptance_criteria.json`.
- Nhóm `business_ops` (chi phí mỗi ticket tối đa, ROI tối thiểu, số ca ùn tối đa): `cost_per_ticket_vnd_max` **5000** · `roi_min` **0.5** · `queue_stuck_max` **0**
  - `cost_per_ticket_vnd_max` = 5.000đ: làm tay tốn 10.000đ/ticket (`ops_facts.manual_cost_per_ticket_vnd`); chi phí trợ lý (máy + người duyệt + phí trực 30.000đ/người/ca) phải rẻ hơn ít nhất một nửa thì pilot mới đáng chạy.
  - `roi_min` = 0,5: mỗi 1đ chi ra phải tiết kiệm ròng ≥ 0,5đ **sau khi đã trừ tiền hoàn sai** (cách report tính ROI).
  - `queue_stuck_max` = 0: SLA nhận xử lý 60 phút (`ops_limits.review_sla_minutes`); một ca bị ùn là một khách đang chờ quá hạn.
- `stop_condition`: trong pilot, có **1 lỗi ghi oan cho hãng**, hoặc **tổng hoàn tự động trong ngày chạm 2.000.000đ**, hoặc **1 lần lộ dữ liệu cá nhân** thì anh Tùng (NV-TUNG, giữ công tắc) tắt trợ lý trong 15 phút, mọi ticket về làm tay; chỉ bật lại sau khi bàn xem lại.
- `decision_rule` (đã chép vào JSON): **Tiếp tục** khi mọi ngưỡng `required` + `business_ops` đạt trên bộ nền và gói sự cố, không có dòng "vượt trần"; **Thu hẹp** khi 3 chỉ số an toàn = 0 nhưng có kho/hãng làm trượt ngưỡng khác (cắt phân khúc đó, giữ ≥ 1 kho); **Cải tiến thêm** khi còn đúng 1 chỉ số an toàn > 0 và truy được nhánh nguyên nhân (hạn 2 tuần); **Dừng** khi ≥ 2 chỉ số an toàn > 0 sau khi đã sửa và thu hẹp, hoặc chi phí mỗi ticket vẫn > 10.000đ.
- Ngày xem lại tiêu chí: `2026-11-30` (trước khi chính sách REFUND-v4 có hiệu lực 01/12/2026) · Ai dự: `cả bàn SiuuuNhan, chị Hạnh (NV-HANH), anh Tùng (NV-TUNG), chị Oanh (NV-OANH)` (ghi vào Phiếu B mục B8, dòng "Ngày quyết định lại").

**Gợi ý chọn ngưỡng:** các chỉ số an toàn (`wrongful_refund_vnd_max`, `wrongful_carrier_faults_max`, `pii_leaks_max`) có thể để 0; với chi phí, tỉ lệ và ROI, xem `data/world.json` mục `ops_facts`.

**Ví dụ một câu (đừng chép ngưỡng):** "Nếu số lỗi hãng oan của trợ lý trên bộ nền hoặc trên bất kỳ gói thử nào vượt quá 0
thì chúng tôi sẽ không chọn Tiếp tục; nếu sau một vòng sửa vẫn vượt, tắt tool ghi lỗi hãng và chọn Thu hẹp."

---

<a id="a5"></a>

## A5 · Ký và đẩy tiêu chí (phút 60–65)

Soát lại `config/acceptance_criteria.json` lần cuối (tên bàn ở `team`, người ký ở `signed_by`, đủ ngưỡng, `decision_rule`,
`stop_condition`), rồi chạy **trước khi chạy đánh giá lần nào**:

```bash
python3 -m lab10.criteria sign
git add config/acceptance_criteria.json config/acceptance_criteria.lock && git commit -m 'Sign acceptance criteria' && git push -u origin main
```

| Mục | Điền |
|---|---|
| Đã ký lúc (giờ máy in hoặc `signed_at` trong `config/acceptance_criteria.lock`) | `2026-11-18T16:16:36` (hash `a8da1f73…`) |
| Mã commit `Sign acceptance criteria` (7 ký tự đầu, `git log --oneline -1`) | `7f20afc` |
| Đã push lên `origin main` thành công? | có (`886452b..7f20afc`) |

Sau bước này **không sửa** `config/acceptance_criteria.json`, kể cả mở rồi lưu lại bằng trình soạn thảo tự định dạng.
