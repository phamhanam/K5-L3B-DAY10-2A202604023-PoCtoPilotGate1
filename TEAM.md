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
