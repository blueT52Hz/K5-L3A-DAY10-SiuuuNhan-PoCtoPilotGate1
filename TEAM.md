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

## HoVaTen-MSSV

### Phần việc phụ trách

Vai trong bàn; câu nào của đề, mục nào của phiếu A/B/C, file nào (`lab10/guards.py`, `config/operating_gates.json`, …).

### Đóng góp cụ thể

...

### Bằng chứng

Mã commit, mã lần chạy (`runs/<mã>`), dòng trong phiếu.

### Exit ticket

Một điều học được, một điều còn chưa chắc.

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
