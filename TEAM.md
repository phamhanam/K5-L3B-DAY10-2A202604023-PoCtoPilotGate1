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

Phụ trách **Vận hành và pháp lý** của dự án PoCtoPilotGate, tập trung vào hai cổng `operations` và `legal` trong `config/operating_gates.json`.

Các đầu việc chính:
- Hoàn thiện cấu hình vận hành: người phụ trách (PIC), người duyệt, số lượng nhân sự trực, công suất xử lý, SLA, ghi chú quyết định và tỷ lệ kiểm tra mẫu.
- Xây dựng điều kiện cảnh báo và dừng pilot khi phát sinh các rủi ro vận hành hoặc pháp lý.
- Kiểm soát dữ liệu cá nhân trong payload gửi cho bên vận chuyển và yêu cầu ghi nhận nguyên nhân trước khi quy lỗi cho hãng.
- Phụ trách Phiếu B: B4–B5 và B7.5–B7.6; Phiếu C: C11.
- Tổng hợp thông tin thành viên, vai trò và thông tin repo trong `submission/submission.json`.

### Đóng góp cụ thể

**1. Thiết lập cổng vận hành (`operations`)**

- Phân công NV-TUNG (Lê Thanh Tùng) làm PIC vận hành, chịu trách nhiệm theo dõi hoạt động và xử lý khi cần tắt trợ lý.
- Phân công NV-HANH (Trần Thị Hạnh) làm người duyệt các quyết định vượt hạn mức.
- Đề xuất bố trí 2 người trực, với công suất xử lý mục tiêu 12 ca/giờ.
- Đặt SLA chờ xử lý tối đa 60 phút.
- Bật yêu cầu ghi chú giải thích cho các quyết định và kiểm tra mẫu tối thiểu 10%.
- Xây dựng ngưỡng phản ứng với hàng chờ: khi thời gian chờ vượt 30 phút cần cảnh báo và xem xét bổ sung nhân sự; khi đạt 60 phút cần thu hẹp phạm vi pilot hoặc chuyển sang xử lý thủ công.

**2. Thiết lập cổng pháp lý (`legal`)**

- Xác định dữ liệu cá nhân của người nhận hàng là thông tin không được tự ý chuyển cho bên vận chuyển.
- Giới hạn payload `notify_carrier` trong 4 trường được phép: `order_id`, `parcel_id`, `district`, `delay_days`.
- Chặn các trường thông tin cá nhân như `name`, `phone`, `street`, `address`, `email`, `national_id`, `customer_note` và `recipient_contact`.
- Yêu cầu tắt hoặc chặn hành động `notify_carrier` khi phát hiện payload có thông tin cá nhân không được phép gửi; đồng thời ghi nhận sự cố để kiểm tra.
- Yêu cầu có nguyên nhân và bằng chứng trước khi ghi nhận lỗi thuộc về hãng vận chuyển, tránh quy lỗi khi chưa đủ căn cứ.

**3. Phân tích rủi ro và hoàn thiện checklist**

- Đối chiếu dữ liệu sự cố, cấu hình và luồng xử lý để xác định nguy cơ thông tin người nhận bị đưa vào payload gửi hãng, kể cả khi người đặt hàng không nhập thông tin đó trong ticket.
- Bổ sung các rủi ro về rò rỉ PII, quá tải hàng chờ và mất niềm tin của nhân viên vào risk register.
- Hoàn thiện Phiếu C mục C11 bằng cách rà soát checklist go-live theo 9 nhóm: chất lượng, dữ liệu, bảo mật, quyền hạn, hiệu năng, chi phí, vận hành, con người/pháp lý và quyết định.
- Đề xuất chỉ chuyển sang pilot khi các điều kiện vận hành, bảo mật và pháp lý đã được kiểm tra, có người chịu trách nhiệm và có phương án xử lý khi điều kiện dừng bị kích hoạt.

**4. Tổng hợp bài nộp**

- Tổng hợp họ tên, MSSV và vai trò của các thành viên theo bảng thông tin nhóm.
- Chuẩn hóa danh sách `members` trong `submission/submission.json` theo định dạng `HoVaTen-MSSV`.
- Cập nhật tên repo theo thông tin nhóm: `K5-L3B-DAY10-Sky-PoCtoPilotGate1`.
- Kiểm tra tính thống nhất giữa thông tin thành viên trong README và file submission.

### Bằng chứng

- File cấu hình phụ trách: `config/operating_gates.json`.
- Các nội dung cần đối chiếu: `data/world.json`, `lab10/guards.py`, `lab10/monitors.py`.
- Tài liệu bàn giao: Phiếu B (B4–B5, B7.5–B7.6), Phiếu C (C11) và `submission/submission.json`.
- Commit và mã lần chạy: sẽ cập nhật sau khi hoàn tất kiểm tra, chạy đánh giá và chốt vòng.

### Exit ticket

**Một điều học được:**

Cổng vận hành và pháp lý không chỉ là các điều kiện kỹ thuật trong code. Mỗi điều kiện cần gắn với người chịu trách nhiệm, người có quyền phê duyệt, ngưỡng cảnh báo, kênh thông báo và quy trình dừng cụ thể. Đặc biệt, dữ liệu có sẵn trong hệ thống không đồng nghĩa với dữ liệu được phép chia sẻ cho bên thứ ba.

**Một điều còn chưa chắc:**

Ngưỡng bố trí 2 người trực với công suất 12 ca/giờ và tỷ lệ kiểm tra mẫu 10% hiện là phương án đề xuất. Cần đối chiếu với dữ liệu pilot thực tế về số lượng ticket, thời gian xử lý, tỷ lệ chuyển cấp và số trường hợp vi phạm để xác nhận các ngưỡng này có phù hợp hay không trước Bước đánh giá 2.
