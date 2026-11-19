# Team

## Thông tin nhóm

- Tên nhóm (`TenNhom`, không dấu, không khoảng trắng): Sky  
- Lớp: `L3A` / `L3B` L3B
- Repo của bàn: `K5-<L3A|L3B>-DAY10-<TenNhom>-PoCtoPilotGate1`
- Thẻ sự cố đã bốc (S1–S8):

## Thành viên

Họ tên đầy đủ và MSSV của **mọi** thành viên; bàn 3 người thì để trống dòng 4. Vai: Kỹ sư cổng · Sản phẩm và kinh doanh · Vận hành và pháp lý (README mục 3, phút 0–15).

| STT | Họ và tên | MSSV | Vai | Trưởng nhóm |
| --: | --------- | ---- | --- | :---------: |
|   1 |   Phạm Hà Nam        | 2A202604023     |  Kỹ sư cổng   |             |
|   2 |  Triệu Tuấn Minh         |  2A202604123    |   Kỹ sư cổng  |             |
|   3 |      Nguyễn Ánh Dương     |  2A202604087    |   Sản phẩm và kinh doanh  |             |
|   4 | Nguyễn Anh Tú          |  2A202604088    | Vận hành và pháp lý   |        không     |

Ghi `members` trong `submission/submission.json` theo dạng `"HoVaTen-MSSV"`, khớp bảng trên.

## Cá nhân

Mỗi thành viên tự viết một mục bên dưới (chép mẫu, đổi tiêu đề thành họ tên không dấu và MSSV, ví dụ `## NguyenVanAn-20241234`).

## NguyenAnhTu-2A202604088

### Phần việc phụ trách

Vận hành và pháp lý; cổng `operations` và `legal` trong `config/operating_gates.json`; Phiếu B mục B4–B5 và B7.5–B7.6; Phiếu C mục C11; gom bài nộp trong `submission/submission.json`.

### Đóng góp cụ thể

Thiết lập PIC và người duyệt: NV-TUNG phụ trách vận hành, NV-HANH phụ trách duyệt khoản vượt hạn mức. Đặt hai người trực, công suất 12 ca/giờ, SLA chờ tối đa 60 phút, bật ghi chú giải thích và kiểm mẫu 10%.
Thiết lập điều kiện dừng cho hoàn sai, ghi oan hãng, lộ PII và hàng chờ; chặn dữ liệu người nhận gửi cho hãng và yêu cầu ghi đầy đủ nguyên nhân lỗi trước khi ghi lỗi hãng.
Điền danh sách thành viên và tên repo vào `submission/submission.json`.

### Bằng chứng

Commit và mã lần chạy sẽ được cập nhật sau khi hoàn tất các lệnh kiểm tra và chốt vòng.

### Exit ticket

Một điều học được: cổng vận hành và pháp lý cần gắn tên người, ngưỡng, kênh báo tin và quy trình dừng rõ ràng thay vì chỉ đặt trong code.
Một điều còn chưa chắc: ngưỡng số người trực và tỉ lệ kiểm mẫu cần được đối chiếu dữ liệu pilot thật trước Bước đánh giá 2.

## TrieuTuanMinh-2A202604123

### Phần việc phụ trách

Kỹ sư cổng; triển khai `pre_guard` và `write_gate` trong `lab10/guards.py`, chỉ số theo dõi trong `lab10/monitors.py`; Phiếu B mục B7.1–B7.3 và Phiếu C mục C7–C8.

### Đóng góp cụ thể

- Ghìm chính sách hoàn đang hiệu lực; đối chiếu số tiền/người trả với tracking, đơn hàng và chính sách trước khi ghi hoàn.
- Kiểm tra phê duyệt vượt hạn mức theo ticket, đơn, khách, người duyệt, trạng thái, hạn dùng và số tiền; chuyển người duyệt nếu không hợp lệ. Áp trần hoàn tự động theo khách/ngày.
- Chặn ghi lỗi hãng nếu kiện, hãng, độ trễ hoặc nguyên nhân không khớp dữ liệu tin cậy; thêm monitor `refund_guard_blocks` và `customer_daily_cap_hits`.

### Bằng chứng

- Eval S8 after `R-S8-after-20261119-173736-ef9c2a`: 260/260 đạt, 35/35 tấn công được xử lý, không có hoàn sai, lỗi hãng oan hoặc lộ PII.
- Grade `R-S8-grade-20261119-173839-ef9c2a`: FAIL do kiểm tra integrity và hash tiêu chí đã ký; các kiểm tra visible, regression và monitor trong report đạt.
- `customer_daily_cap_hits` được thêm sau report trên; chưa có lượt eval xác nhận chỉ số mới. Chưa ghi commit hash.

### Exit ticket

Một điều học được: cổng phải kiểm tra nguồn dữ liệu có thẩm quyền ngay trước lệnh ghi; log và monitor cần dùng đúng loại sự kiện mà guard phát ra.
Một điều còn chưa chắc: monitor mới cần được chạy lại trên bộ nền và S8 để xác nhận số đếm; grade cũng cần xử lý điều kiện integrity và chữ ký tiêu chí trước khi có thể kết luận đạt.