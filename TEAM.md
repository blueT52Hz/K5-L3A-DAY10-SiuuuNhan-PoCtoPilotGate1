# Team

## Thông tin nhóm

- Tên nhóm (`TenNhom`, không dấu, không khoảng trắng): `SiuuuNhan`
- Lớp: `L3A`
- Repo của bàn: `K5-L3A-DAY10-SiuuuNhan-PoCtoPilotGate1`
- Thẻ sự cố đã bốc (S1–S8):

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

Trưởng nhóm, vai **Vận hành và pháp lý** (TV1), giữ git của bàn.

- Phiếu A: câu 1.2 (A1, mục tiêu của chị Oanh và chị Hạnh), câu 1.4 (A2 cột Telemetry production).
- Phiếu B: câu 2.4 (B4 HAZOP vòng 1, B5 checklist 9 nhóm việc), câu 2.5 ghi pre-mortem (B6, các lăng kính Kỹ thuật, Con người và vận hành, Pháp lý), câu 2.10 (B7.5 runbook 1-3, B7.6 giờ cao điểm). File: `config/operating_gates.json` mục `operations`, `legal`.
- Phiếu C: phần riêng của thẻ, câu 3.3, câu 3.7 (C9-C11, runbook 4-5). File: `submission/submission.json`.
- Làm thêm phần việc còn trống của Kỹ sư cổng ở buổi sáng 19/11 để kịp hạn: chạy mốc base (B0, B1), câu 1.3, 1.5, cổng vòng 1 trong `lab10/guards.py` (B7.1), chốt vòng 1, mốc prepared và quyết định v1 (B8, phần còn trống), kéo thẻ S3, Phiếu C còn lại (C0-C2, C4-C8, C12), Cổng 4 vòng 2, chỉ số theo dõi trong `lab10/monitors.py`, lệnh 7.

### Đóng góp cụ thể

- Tạo repo, mời thành viên, gắn `upstream`, đặt danh tính Git; điền bảng thành viên.
- Cổng `operations`: PIC `NV-TUNG`, người duyệt `NV-HANH`, 1 người trực, 6 ca/giờ, chờ tối đa 60 phút, 5 điều kiện dừng khớp `stop_condition` đã ký, kênh báo tin `#logix-hoantien-pilot-canhbao`, ghi chú giải thích, kiểm mẫu 10%. Cổng `legal`: chặn `recipient_contact`, `customer_note` khi gửi hãng; chỉ ghi lỗi hãng khi tracking có nguyên nhân.
- HAZOP vòng 1 trên `file_carrier_fault` (5 guideword, 4 dòng ngoài kỹ thuật); checklist 9 nhóm việc, mỗi dòng một PIC có tên.
- Runbook 1-3 và giờ cao điểm dùng đúng ngưỡng đã ký (chi phí ≤ 5.000đ, ROI ≥ 0,5, dừng trong 15 phút do NV-TUNG bấm).

### Bằng chứng

- Commit: `20f0284` (bảng thành viên), `19e6c35` b5 (câu 1.2), `a2a0d9c` b7 (câu 1.4), `8feb6f3` b15 (B4, B5), `0d8d575` b16 (B6), `b8c40a4` b21 (`operations`, `legal`, runbook 1-3, giờ cao điểm).
- Commit ngày 19/11: `46f34f0` b17 (cổng vòng 1), `79085d1` b22 (chốt vòng 1, hash `04f5e8a3`), `30019a3`, `5f9c819` (câu 1.3, 1.5, B0, B1, B7.1, B8), `0465f8e` b25 (thẻ S3), `293d156` b32 (Cổng 4), `d4341a0` b34, `4d5fb71` b35 (`monitors.py`), các commit Phiếu C và bài nộp.
- Mã lần chạy (`runs/<mã>`): base `R-base-before-20261119-110440-cccac5`, prepared `R-base-prepared-20261119-110504-096b9e`; thẻ S3 grade `R-S3-grade-20261119-110757-1b7ad5` (PASS-VISIBLE).
- Dòng trong phiếu: A1 câu 1.2, A2; A3; B0, B1, B4, B5, B6, B7.1, B7.5, B7.6, B8; Phiếu C.

### Sử dụng AI

Dùng Claude Code để đọc đề và code của lab, nháp câu chữ cho câu 1.2, 1.4, HAZOP, checklist, pre-mortem, runbook, và chạy lệnh git. Mọi con số trong `operations` lấy từ `data/world.json` (`ops_limits`, `ops_facts`, `staff`) và từ tiêu chí đã ký; mình đã đọc lại và chịu trách nhiệm giải thích lúc demo.

### Exit ticket

Học được: cổng con số và quy trình người (điều kiện dừng, ai bấm công tắc, trong bao nhiêu phút) quan trọng ngang cổng code; runbook phải dùng đúng số trong config và tiêu chí đã ký.

Còn chưa chắc: người duyệt có kịp xử lý các ca trợ lý chuyển sang khi lượng việc tăng gấp ba, vì chưa có số hàng chờ thật từ report.

## NguyenNgocHieu-2A202603502

### Phần việc phụ trách

Vai **Sản phẩm và kinh doanh** (TV4).

- Phiếu A: câu 1.1 và 1.6 (mục A1, A4), ký tiêu chí (A5). File: `config/acceptance_criteria.json`.
- Phiếu B: câu 2.3 (B3), dòng Kinh doanh của pre-mortem (B6), câu 2.9 (B7.4), đề xuất ticket hiểm cho behavioral test cùng TV3 (B7.3), quyết định v1 (B8, *sẽ làm*). File: `config/operating_gates.json` mục `business`.
- Phiếu C: câu 3.2 (C5), phần `business` của C7, quyết định v2 (C12) *(sẽ cập nhật sau vòng 2)*.

### Đóng góp cụ thể

- Viết Bản tiêu chí và điền `config/acceptance_criteria.json`: pass_rate ≥ 0,90, pass_k ≥ 0,85, hoàn sai, lỗi oan cho hãng và lộ dữ liệu cá nhân đều bằng 0; `escalation_rate` ≤ 0,25; `business_ops`: chi phí ≤ 5.000đ/ticket, ROI ≥ 0,5, số ca ùn = 0; điều kiện dừng và `decision_rule` cho 4 quyết định. Chạy lệnh ký và push.
- Bản đồ dữ liệu và ví dụ drift REFUND-v3 → REFUND-v4 (hiệu lực 01/12/2026) ở B3.
- Cổng `business`: trần hoàn 1.500.000đ/ngày, ngân sách 1.500đ/ticket, phạm vi `all`, ROI ≥ 0,5; mỗi số có lý do ở B7.4.
- Sửa định nghĩa "lỗi hãng oan": bản đầu viết "chỉ khi `cause` = CARRIER", mâu thuẫn với nhãn T-006 (FORCE_MAJEURE, REFUND-v3 đòi ghi lỗi MKD); đã sửa theo `fault_causes` của chính sách đang hiệu lực ở A4 và B7.3.

### Bằng chứng

- Commit: `214488d` (Phiếu A và bản nháp tiêu chí), `228a61c` (B3, B6), `886452b` (B7.4 và cổng `business`), `7f20afc` (ký tiêu chí lúc 2026-11-18T16:16:36), `8e95766` (sửa định nghĩa lỗi hãng), `ad67424` (A5).
- Mã lần chạy (`runs/<mã>`): *(bổ sung khi có: base, prepared, after)*.
- Dòng trong phiếu: A1, A4, A5; B3, B6 (dòng Kinh doanh), B7.4; *(bổ sung sau: B8, C5, C7, C12)*.

### Sử dụng AI

Dùng Claude Code để đọc đề và code, nháp ngưỡng và câu chữ cho Phiếu A (A1, A4), bản đồ dữ liệu B3, giá trị cổng `business` (B7.4), câu chữ ticket hiểm B7.3, và để soát lỗi (đối chiếu định nghĩa lỗi hãng với nhãn T-006). Người ký tiêu chí: mình. Lý do từng con số ghi ở Phiếu A (A4) và Phiếu B (B7.4).

### Exit ticket

Học được: tiêu chí phải ký trước khi đo, và định nghĩa "lỗi oan" phải bám chính sách đang hiệu lực (`fault_causes`) chứ không bám một nguyên nhân cố định. Câu "chỉ CARRIER" của mình mâu thuẫn với nhãn T-006.

Còn chưa chắc: các ngưỡng 0,90 / 0,85 / 5.000đ / ROI 0,5 được chọn trước khi xem số, nên chưa biết có quá chặt hay quá lỏng so với mốc base thật; sẽ đối chiếu khi có report.
