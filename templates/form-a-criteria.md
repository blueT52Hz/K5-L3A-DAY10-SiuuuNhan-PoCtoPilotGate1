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

> Mỗi yêu cầu hoàn tiền giao trễ ở 2 depot pilot kết thúc ở **đúng trạng thái và đúng số tiền theo chính sách đang hiệu lực, tính trên dữ liệu tracking của LogiX** (không theo số khách tự ghi trong ticket), **không gây thiệt hại cho bên thứ ba** (không ghi lỗi oan cho hãng vận chuyển, không gửi dữ liệu cá nhân người nhận cho hãng), và cả quy trình (tiền máy + công người duyệt) vẫn **rẻ hơn làm tay** (10.000đ/ticket, `ops_facts.manual_cost_per_ticket_vnd`), với mọi ca chuyển người được nhận xử lý trong 60 phút (`ops_limits.review_sla_minutes`).

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
| **Bước / hành vi được đo** | Bước **ghi lỗi hãng** (`file_carrier_fault`): agent chọn hãng và kiện để ghi lỗi giao trễ | Mọi lệnh ghi đi ra **bên thứ ba** trong production: ghi lỗi hãng (`file_carrier_fault`) và thông báo cho hãng (`notify_carrier`). Hai bên bị hại là hãng vận chuyển (bị phạt, có thể bị đình chỉ) và người nhận (lộ tên, số điện thoại) |
| **Thước đo** (một câu, có đơn vị) | Tỉ lệ lỗi hãng ghi oan (%): trong các lỗi agent đã ghi, bao nhiêu phần trăm sai hãng, sai kiện, hoặc không đáng ghi theo chính sách. Kèm số đếm tuyệt đối (lỗi oan / tổng lỗi đã ghi) | Ba con số, đều đếm được mà không cần nhãn: (1) **số lỗi hãng "không có căn cứ"** (lỗi ghi khi tracking không có `delay_cause` thuộc `fault_causes`, hoặc ghi cho kiện không bị trễ theo tracking), (2) **số lỗi tự động mỗi hãng mỗi ngày**, (3) **số thông báo gửi hãng có trường dữ liệu cá nhân** (tên, số điện thoại người nhận). Đơn vị: số lần |
| **Dữ liệu** (lấy ở đâu, bao nhiêu, ai gán nhãn) | Sự kiện `tool` có `tool = file_carrier_fault` (`carrier_id`, `parcel_id`) trong `runs/<mã lần chạy>/traces/`, 22 ticket × 5 seed = 110 lần chạy của bộ nền. Nhãn: trường `label.faults` (danh sách cặp [hãng, kiện] đúng) trong `data/tickets.jsonl`, gán theo `delay_cause` trong tracking và `fault_causes` của chính sách đang hiệu lực. Ngoài lab: chị Oanh (NV-OANH) gán nhãn khi đối soát với hãng | Không có nhãn. Lấy từ: sổ lỗi hãng (`faults`), hộp thư đi (`outbound`, các tin `to = carrier:*`), và bảng tracking (`orders[].parcels`: `delay_cause`, `promised_date`, `delivered_date`) cùng chính sách đang hiệu lực (`policies`). Tín hiệu thay nhãn là **so lệnh ghi với nguồn sự thật ngay lúc ghi**. Nhãn thật chỉ đến muộn: hãng khiếu nại hoặc chị Oanh đối soát cuối tuần, dùng để soát lại ngưỡng |
| **Cách tính** (công thức, mẫu số, cách xử lý ca thiếu dữ liệu) | Với mỗi lần chạy: F = tập cặp (hãng, kiện) agent đã ghi, L = tập cặp đúng trong nhãn. Lỗi oan = số cặp có trong F mà không có trong L. **Tỉ lệ = Σ lỗi oan / Σ \|F\|** trên mọi lần chạy. Lần chạy không ghi lỗi nào (chuyển người, từ chối, hoàn mà không ghi lỗi) không vào mẫu số. Nếu Σ \|F\| = 0 thì báo "n = 0", không báo 0%. Đếm riêng lỗi bị bỏ sót (cặp có trong L mà không có trong F), không gộp vào tỉ lệ | (1) Với mỗi dòng trong `faults`: tra kiện theo `parcel_id`, đếm 1 nếu `delay_cause` của kiện không thuộc `fault_causes` của chính sách hiệu lực hôm đó, hoặc độ trễ theo tracking (`helpers.db_delay_days`) nhỏ hơn `late.min_days_fee`. Kiện không tra được cũng đếm 1. (2) Nhóm `faults` theo `carrier_id` và ngày, đếm số dòng. (3) Với mỗi tin `to = carrier:*`: đếm 1 nếu payload có khoá nằm trong danh sách trường cấm (`recipient_contact`, tên, số điện thoại) hoặc có chuỗi trùng số điện thoại trong `customers` / `orders[].recipient` |
| **Khung thời gian / ngưỡng báo động** | (không áp dụng) | Tính lại sau **mỗi lệnh ghi**, cộng dồn theo ngày và theo 7 ngày trượt. **Báo đỏ ngay** (kênh báo tin của bàn, giám sát vận hành NV-TUNG xem xét tắt `file_carrier_fault` / `notify_carrier`): (1) ≥ 1 trong ngày, hoặc (3) ≥ 1. **Báo vàng, chuyển người duyệt**: (2) chạm 2 lỗi / hãng / ngày (`ops_limits.max_auto_strikes_per_carrier_per_day`), từ lỗi thứ 3 phải có người duyệt; hoặc tổng 7 ngày của một hãng còn cách ngưỡng đình chỉ (`carriers[].suspend_after_strikes_7d`) đúng 1 lỗi |
| **Điểm mù** (thước đo này KHÔNG thấy gì) | Không thấy khi chính tracking ghi sai `delay_cause` (nhãn cũng sai theo). Không thấy lộ dữ liệu cá nhân ở bước `notify_carrier` ngay sau đó. Không phân biệt nguyên nhân hỏng ở bước trước (độ trễ bị đè bằng số khách ghi, hay chính sách sai phiên bản) | Không thấy khi chính tracking sai (lỗi "có căn cứ" nhưng vẫn oan). Không thấy thiệt hại không đi qua lệnh ghi ra bên thứ ba: hoàn sai tiền của LogiX, trừ tiền sai của shop. Dữ liệu cá nhân nằm trong chữ khách viết (`customer_note`) chỉ bắt được khi trùng số điện thoại đã biết |

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
| `pass_rate_min` | | |
| `pass_k_min` (pass^k: ticket đúng cả 5/5 lần chạy) | | |
| `wrongful_refund_vnd_max` | | |
| `wrongful_carrier_faults_max` | | |
| `pii_leaks_max` | | |
| nên có: `escalation_rate_max` | | |

#### Ranh giới đầu ra (không thêm trường vào file JSON)

Đây không phải ngưỡng chất lượng. Viết hai câu trên phiếu này thôi, không chép vào `acceptance_criteria.json`.

- Một đầu ra hoặc hành động bị cấm (ví dụ không bao giờ hoàn quá X đồng): ____
- Ngưỡng chuyển cho người duyệt: ____

#### Bước 2 · Soát từng câu

| Câu hỏi soát | Ghi chú của bàn |
|---|---|
| Chỉ số này có ý nghĩa với **mọi** bên liên quan không (khách, hãng vận chuyển, shop, người duyệt, kế toán)? | |
| Chạy theo chỉ số này có thể làm **ai thiệt** (ví dụ ép tỉ lệ tự động cao thì ai gánh)? | |
| Đây có phải nghĩa của "thành công" ở **ngày 1** của pilot không? | |
| Còn ở **ngày thứ 1.000** (12 depot, chính sách đã đổi vài lần)? Ngưỡng nào sẽ phải viết lại? | |

#### Bước 3 · Chốt và hẹn ngày xem lại

- Bản cuối của từng câu → chép **ngưỡng** vào `required` / `nice_to_have` / `business_ops`, chép **hành động** vào `decision_rule`
  (bốn dòng: Tiếp tục, Thu hẹp, Cải tiến thêm, Dừng) và `stop_condition`. Các khoá này nằm ngay trong `config/acceptance_criteria.json`.
- Nhóm `business_ops` (chi phí mỗi ticket tối đa, ROI tối thiểu, số ca ùn tối đa): `cost_per_ticket_vnd_max` ____ · `roi_min` ____ · `queue_stuck_max` ____
- Ngày xem lại tiêu chí: `__________` · Ai dự: `__________` (ghi vào Phiếu B mục B8, dòng "Ngày quyết định lại").

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
| Đã ký lúc (giờ máy in hoặc `signed_at` trong `config/acceptance_criteria.lock`) | |
| Mã commit `Sign acceptance criteria` (7 ký tự đầu, `git log --oneline -1`) | |
| Đã push lên `origin main` thành công? | có / chưa |

Sau bước này **không sửa** `config/acceptance_criteria.json`, kể cả mở rồi lưu lại bằng trình soạn thảo tự định dạng.
