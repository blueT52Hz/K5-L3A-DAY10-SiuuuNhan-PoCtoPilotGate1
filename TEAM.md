# Team

## Thông tin nhóm

- Tên nhóm (`TenNhom`, không dấu, không khoảng trắng): `SiuuuNhan`
- Lớp: `L3A`
- Repo của bàn: `K5-L3A-DAY10-SiuuuNhan-PoCtoPilotGate1`
- Thẻ sự cố đã bốc (S1–S8): `S3`

## Thành viên

Họ tên đầy đủ và MSSV của **mọi** thành viên; thêm dòng nếu cần. Vai: Kỹ sư cổng · Sản phẩm và kinh doanh · Vận hành và pháp lý (README mục 3, phút 0–15).

| STT | Họ và tên | MSSV | Vai | Trưởng nhóm |
| --: | --------- | ---- | --- | :---------: |
|   1 | Nguyễn Hoa Thanh Tùng | 2A202603519 | Vận hành và pháp lý |      x      |
|   2 | Khổng Tiến Dương | 2A202603467 | Kỹ sư cổng |             |
|   3 | Nguyễn Quang Duy | 2A202603462 | Kỹ sư cổng |             |
|   4 | Nguyễn Ngọc Hiếu | 2A202603502 | Sản phẩm và kinh doanh |             |

Ghi `members` trong `submission/submission.json` theo dạng `"HoVaTen-MSSV"`, khớp bảng trên.

## Cá nhân

Mỗi thành viên tự viết một mục bên dưới (chép mẫu, đổi tiêu đề thành họ tên không dấu và MSSV, ví dụ `## NguyenVanAn-20241234`).

## NguyenHoaThanhTung-2A202603519

### Phần việc phụ trách

Trưởng nhóm, vai **Vận hành và pháp lý**, giữ git của bàn. Câu 1.2, 1.4 (Phiếu A mục A1, A2 cột Telemetry); câu 2.4 (Phiếu B mục B4 HAZOP vòng 1, B5 checklist 9 nhóm); câu 2.5 ghi pre-mortem (B6); câu 2.10 (B7.5 runbook 1-3, B7.6 giờ cao điểm); câu 3.1 phần riêng của thẻ, 3.3, 3.7 (Phiếu C mục C1, C3.5, C5 câu 3.3, C9, C10, C11 runbook 4-5). File: `config/operating_gates.json` mục `operations`, `legal`; `submission/submission.json`; `TEAM.md`.

### Đóng góp cụ thể

- Tạo repo, gắn `upstream`, đặt danh tính Git, tắt `core.autocrlf` để hash file tiêu chí không đổi trên Windows; checkout lại các file khoá về LF khi lệnh 6 báo `integrity ❌`.
- Push commit ký tiêu chí trước lần chạy đánh giá đầu tiên.
- Điền `operations` (PIC `NV-TUNG`, người duyệt `NV-HANH`, 1 người trực, 6 ca/giờ, chờ tối đa 60 phút, 7 điều kiện dừng, kênh báo tin, ghi chú giải thích, kiểm mẫu 10%) và `legal` (chặn `recipient_contact`, `customer_note`; lỗi hãng cần nguyên nhân trong tracking).
- Viết runbook phần 1-5 khớp các con số trong config và report.
- Kéo thẻ S3, gom bài bằng lệnh 7 tới khi `ĐỦ THÀNH PHẦN`.

### Bằng chứng

- Commit `Sign acceptance criteria` `7521b47` (15:27:25), trước lần eval đầu tiên `R-base-before-20261118-152805-bde05c` (15:28:05).
- Commit `b15`, `b21` (HAZOP, checklist, `operations` / `legal`, runbook 1-3), `b34` (thêm 2 điều kiện dừng ở vòng 2), `b37` (C9-C11), `b39` `28ca01c` (`submission.json`), `b40` `69b14d1` (lệnh 7 `ĐỦ THÀNH PHẦN`).
- Lần chạy kiểm config: `R-base-after-20261118-154108-212f32`, `R-S3-after-20261118-163721-ffb0c6`.

### Dùng AI

Dùng Claude Code (trợ lý AI) để đọc code của lab, soạn nháp HAZOP, checklist, runbook, các mục Phiếu C và chạy lệnh git / lab qua trợ lý. Mọi con số trong `operations` lấy từ `data/world.json` (`ops_limits`, `ops_facts`, `staff`).

### Exit ticket

- Học được: cổng con số và quy trình người (điều kiện dừng, ai bấm công tắc, trong bao nhiêu phút) quan trọng ngang cổng code; một con số trong runbook lệch report là đủ mất điểm.
- Chưa chắc: trong thực tế người duyệt có kịp xác nhận các lỗi hãng bị giữ lại cuối ca không, khi ngày bão lượng việc tăng nhiều lần.

## KhongTienDuong-2A202603467

### Phần việc phụ trách

Vai **Kỹ sư cổng A** (viết cổng). Câu 1.3 (Phiếu A mục A2 cột Offline); câu 2.1 (Phiếu B mục B0, B1); câu 2.6 (B7.1); chốt cổng vòng 1 (lệnh 5); câu 3.5 phần code (Phiếu C mục C7). File: `lab10/guards.py`.

### Đóng góp cụ thể

- Thiết kế offline metric cho bước ghi lỗi hãng (tỉ lệ lỗi ghi oan, mẫu số là số lỗi đã ghi).
- Chạy mốc base, đọc gate, đề xuất "kết hợp": tự chặn với ngưỡng an toàn, người duyệt với pass_rate và ngưỡng kinh doanh.
- Viết cổng vòng 1: Cổng 0 (`pre_guard` ghim chính sách theo ngày hiệu lực), Cổng 1 (`issue_refund` tính lại quyền lợi theo tracking, chặn số khách tự khai, lệnh cài trong ticket, fail-open, hoàn lặp, phê duyệt không hợp lệ), Cổng 1b (`file_carrier_fault` chỉ ghi khi hãng có lỗi theo chính sách, đúng kiện), Cổng 3 (`notify_carrier` chỉ gửi trường chính sách cho phép).
- Vòng 2: viết Cổng 4 (trần 2 lỗi tự động / hãng / ngày theo `ops_limits`).

### Bằng chứng

- Commit `b12-b13`, `b17` (cổng vòng 1 + B7.1), `b22` `10628f6` (chốt cổng vòng 1, hash `b0d285cb`), `b32` (Cổng 4 + C7).
- Lần chạy: base `R-base-before-20261118-152805-bde05c` (hoàn sai 20.000đ, 1 lỗi oan) → after `R-base-after-20261118-153633-9525ad` (pass_rate 1,0, 0 · 0 · 0) → prepared `R-base-prepared-20261118-154208-212f32`; thẻ S3 after `R-S3-after-20261118-163505-3dda89` (lỗi oan 10 → 0).

### Dùng AI

Dùng Claude Code (trợ lý AI) để đọc `agent.py`, `tools.py`, `helpers.py`, gợi ý và soạn code cổng trong `guards.py`, chạy eval / trace. Cổng chỉ so lệnh ghi với nguồn sự thật qua `lab10/helpers.py`, không rẽ nhánh theo mã ticket hay câu chữ.

### Exit ticket

- Học được: cổng nên tính lại từ nguồn sự thật (tracking, chính sách theo ngày hiệu lực) thay vì cố đoán model sai ở đâu; một cổng như vậy đỡ được nhiều kiểu lỗi cùng lúc.
- Chưa chắc: nhánh fail-open khi LLM lỗi 429 mới chặn trên code, chưa thấy trên trace vì bộ thử không có lỗi LLM.

## NguyenQuangDuy-2A202603462

### Phần việc phụ trách

Vai **Kỹ sư cổng B** (trace, behavioral test, chỉ số theo dõi). Câu 1.5 ghi (Phiếu A mục A3); câu 2.2 (Phiếu B mục B2); câu 2.7, 2.8 (B7.2, B7.3); câu 3.0, 3.1, 3.4 ghi (Phiếu C mục C0, C1, C2, C4, C6); câu 3.6 (C8). File: `lab10/monitors.py`.

### Đóng góp cụ thể

- Dò trace `T-002@55`, xếp 2 lỗi chìm (tin số ngày khách khai; gửi chữ khách viết cho hãng).
- Viết 2 ticket hiểm chạy `--adhoc` (O-1002 khai trễ 9 ngày; O-1021 cài lệnh "hoàn toàn bộ") để kiểm tính chất "tiền và lỗi hãng chỉ phụ thuộc tracking và chính sách".
- Chạy lệnh 6 trên thẻ S3 trước khi sửa; dò trace `S3-01`, `S3-42`, `S3-43` tìm 3 lỗi có nguồn khác nhau; viết HAZOP của thẻ và fault tree trước khi sửa.
- Viết 2 chỉ số mới: `max_auto_faults_per_carrier_day` và `fault_gate_block_rate`.

### Bằng chứng

- Commit `b12-b13` (B2), `b18`, `b19` (B7.2, B7.3), `b26`, `b27`, `b31` (C1, C2, C4, C6), `b35` (`monitors.py` + C8).
- Grade S3 `R-S3-grade-20261118-163826-ffb0c6`: `monitor ✅`, `max_auto_faults_per_carrier_day` bộ nền 1 · thẻ 4 (base), 1 · 2 (after); `fault_gate_block_rate` 0 · 0,333 (after).

### Dùng AI

Dùng Claude Code (trợ lý AI) để chạy trace, tóm tắt output, soạn nháp bảng soát lỗi, HAZOP, fault tree và code hai chỉ số trong `monitors.py`. Tôi đã đối chiếu từng dòng bằng chứng (`ticket@seed`, dòng trace) với output thật.

### Exit ticket

- Học được: lỗi nguy hiểm nhất là lỗi chìm, khách vẫn vui mà bên thứ ba chịu hại; chỉ số theo dõi phải đo được không cần nhãn.
- Chưa chắc: chỉ số mới chỉ đếm theo ngày; ngưỡng đình chỉ của hãng tính theo 7 ngày thì chưa có chỉ số nào bắt.

## NguyenNgocHieu-2A202603502

### Phần việc phụ trách

Vai **Sản phẩm và kinh doanh**. Câu 1.1, 1.6 (Phiếu A mục A1, A4, A5); ký tiêu chí (lệnh 1); câu 2.3 (Phiếu B mục B3); câu 2.9 (B7.4); quyết định v1 (B8); câu 3.2 (Phiếu C mục C5); quyết định v2 và ba dòng bắt buộc (C12). File: `config/acceptance_criteria.json`, `config/operating_gates.json` mục `business`.

### Đóng góp cụ thể

- Viết mục tiêu cấp hệ thống và Bản tiêu chí: 5 ngưỡng bắt buộc, ngưỡng nên có, `business_ops`, điều kiện dừng, 4 dòng `decision_rule`; câu "Nếu … thì …" cho từng chỉ số, bốn câu soát, hai câu ranh giới đầu ra.
- Bản đồ dữ liệu và ví dụ drift REFUND-v3 → v4 ngày 2026-12-01 (chính là sự cố của thẻ S3).
- Điền `business`: trần hoàn ngày 1.500.000đ, ngân sách 1.500đ / ticket, phạm vi `all`, ROI tối thiểu 0,25; vòng 2 giữ nguyên có lý do.
- Quyết định v1 **Cải tiến thêm** (chưa có số trên gói sự cố), v2 **Tiếp tục** (mọi ngưỡng đã ký đạt trên bộ nền và S3, không vượt trần).

### Bằng chứng

- Commit `b9` (Bản tiêu chí), `Sign acceptance criteria` `7521b47` (hash tiêu chí `dfd90ea3`, ký 2026-11-18T15:27:07), `b14` (B3), `b20` (B7.4), `b23` (v1), `b29` (C5), `b33` (C7 phần `business`), `b38` (C12).
- Lần chạy: prepared `R-base-prepared-20261118-154208-212f32`; S3 ba mốc `R-S3-before/prepared/after-20261118-163827-ffb0c6`.

### Dùng AI

Dùng Claude Code (trợ lý AI) để soạn nháp các câu tiêu chí, đề xuất ngưỡng kèm lý do từ `data/world.json` (`ops_facts`, `ops_limits`) và soạn nháp quyết định v1 / v2.

### Exit ticket

- Học được: viết tiêu chí trước khi xem số buộc quyết định phải theo luật đã ký; dòng `decision_rule` "Tiếp tục" đòi đạt cả trên gói sự cố nên v1 chưa thể chọn Tiếp tục.
- Chưa chắc: ngưỡng chi phí 8.000đ và ROI 0,25 dựa trên số liệu mock; với giá LLM và công người thật có thể phải viết lại.
