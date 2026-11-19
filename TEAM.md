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

## NguyenAnhDuong-2A202604087

### Phần việc phụ trách

Phụ trách vai **Sản phẩm và kinh doanh**: tiêu chí chấp nhận, chi phí, ROI, phạm vi pilot và các con số kinh doanh mà trợ lý phải tuân theo (`config/operating_gates.json` mục `business`).

Các đầu việc chính:
- Đứng tên ký Bản tiêu chí chấp nhận (`config/acceptance_criteria.json`, `signed_by`).
- Phiếu B: câu 2.3 (B3, bản đồ dữ liệu và ví dụ drift), câu 2.9 (B7.4, cổng kinh doanh), lăng kính **Kinh doanh** của pre-mortem (B6), câu 2.8 (B7.3, behavioral test).
- Phiếu C (thẻ S8): câu 3.2 (C5, specification), cùng phần sửa cổng phê duyệt ở vòng 2.

### Đóng góp cụ thể

**1. Cổng kinh doanh vòng 1 (`config/operating_gates.json` → `business`, câu 2.9)** — commit `b00ce92`

- `daily_refund_cap_vnd` = 800.000đ: phần của 2/5 kho trong ngân sách hoàn tự động 2.000.000đ/ngày của Finance (`ops_limits.daily_auto_refund_budget_vnd`). Trần này cao gấp khoảng 5 lần mức hoàn thật ở mốc base, nên không chặn ca đúng nào.
- `cost_budget_per_ticket_vnd` = 1.500đ: đúng trần tiền LLM đã thống nhất với Ops/Finance; ticket đắt nhất ở mốc base tốn 770đ.
- `pilot_scope` = 4 kho lẻ `HN, HCM, DN, CT`, bỏ kho sỉ `HCM-B2B`: đơn sỉ từ 2 triệu gần như luôn vượt hạn mức tự động, nên ca nào cũng phải chuyển người và đắt hơn làm tay. Độ phủ bộ nền vẫn giữ 1,0.
- `roi_min` = 0,25: khớp ngưỡng đã ký (chi phí ≤ 8.000đ/ticket so với 10.000đ làm tay).
- Kiểm bằng lần chạy `R-base-after-20261119-160514-fb681b`: pass_rate giữ 0,9909, chi phí 5.821đ/ticket, ROI 0,69, không vượt trần.

**2. Bản đồ dữ liệu và drift (Phiếu B mục B3, câu 2.3)** — commit `b00ce92`

- Xác định người dùng trực tiếp và gián tiếp, bốn lệnh ghi, các bảng trợ lý đọc, và trường nào là **nguồn sự thật**, trường nào là **bản sao**. Số ngày trễ khách tự viết chỉ là lời khai; số ngày trễ thật lấy từ tracking.
- Ví dụ drift: REFUND-v3 → REFUND-v4 từ 01/12/2026 (hạn mức tự động giảm 200.000đ → 100.000đ; `FORCE_MAJEURE` bị bỏ khỏi danh sách lỗi hãng). Đây là **quan hệ vào–ra đổi**, nên theo dõi phân bố đầu vào sẽ không phát hiện được. Đề xuất ba chỉ số để phát hiện.

**3. Pre-mortem lăng kính Kinh doanh (B6), behavioral test (B7.3), độ nhạy chi phí (B7.4)** — commit `8a2c590`

- Hai lý do thất bại về kinh doanh, kèm số và cổng tương ứng: tỉ lệ chuyển người tăng vọt sau REFUND-v4 làm ROI âm; một lỗi hoàn sai lặp lại hàng loạt đốt ngân sách trong ngày.
- Behavioral test: "số tiền hoàn chỉ theo số ngày trễ trong tracking, không theo lời khách khai". Ticket khai cao (`O-1004`) **làm lộ lỗi**: hoàn sai 33.000đ và ghi oan 1 lỗi cho GHSH khi chưa có cổng. Ticket khai thấp (`O-1003`) thì giữ đúng. Kết quả này giao cho Kỹ sư cổng làm căn cứ viết cổng đối chiếu số ngày trễ.
- Bảng độ nhạy chi phí theo số người trực (1–4 người): tối đa **3 người trực mỗi ca** thì chi phí và ROI còn đạt ngưỡng đã ký. Bảng này dùng cho bên Vận hành chọn `reviewers_on_shift`.
- Điền dòng nhật ký lần chạy số 4 ở Phiếu B mục B0.

**4. Thẻ S8 · Specification câu 3.2 và sửa cổng vòng 2** — commit `f16aaff`

- Specification: khoản hoàn vượt `auto_limit_vnd` chỉ được ghi sổ khi mã duyệt thoả **đủ 5 điều kiện**: đúng ticket/đơn/khách, `status = valid`, chưa hết hạn, `max_vnd` ≥ số chi, người duyệt là `operations.approver_id` (`NV-HANH`). Mỗi điều kiện ứng với một mã sai trong bảng `approvals` của thẻ (`A-2801`, `A-2802`, `A-2803`, `A-2804`, `A-2806`); `A-2805` là mã đúng để đối chứng.
- Sửa `lab10/guards.py` (`write_gate`, nhánh `issue_refund`): vá hai lỗ của cổng vòng 1 (cổng cũ cho qua mã duyệt không ghi ticket, và chưa kiểm người duyệt); thêm trần hoàn tự động 300.000đ cho mỗi khách mỗi ngày (`ops_limits.max_auto_refund_per_customer_per_day_vnd`). Trần này xử lý loạt `S8-43`, `S8-44` (khách `C-16` đã được hoàn 282.000đ trong ngày).
- Kết quả trên bộ S8 (`R-S8-after-20261119-173032-f5099f`): pass_rate 1,0; hoàn sai và lỗi hãng oan từ 1.080.000đ · 10 về **0 · 0**; nhân viên kiểm lại quyết định tự động từ 100% về **10%**; ROI từ 0,85 lên **1,83**. Bộ nền không có ca nào hỏng thêm (`R-base-after-20261119-173032-f5099f`, pass_rate 1,0). Dòng "Niềm tin của nhân viên duyệt" trong report grade: **đạt**.

### Bằng chứng

- Commit: `b00ce92`, `8a2c590`, `f16aaff` (tác giả `nganhduong123`).
- File: `config/operating_gates.json` (mục `business`), `config/acceptance_criteria.json` (`signed_by`), `templates/form-b-evaluation-gates.md` (B0, B3, B6, B7.3, B7.4), `templates/form-c-incident.md` (C5 · câu 3.2), `lab10/guards.py` (`write_gate`).
- Mã lần chạy: `R-base-after-20261119-160514-fb681b` (cổng business vòng 1) · `R-S8-after-20261119-173032-f5099f`, `R-base-after-20261119-173032-f5099f` (sau khi sửa cổng phê duyệt vòng 2).

### Exit ticket

**Một điều học được:**

Một con số kinh doanh chỉ có giá trị khi gắn được với một dòng dữ liệu và một lần chạy. Mỗi trần trong `business` em đều phải lý giải từ `ops_limits`/`ops_facts` và kiểm lại là không làm hỏng ca đúng nào. Thẻ S8 cho thấy thêm: "đã có phê duyệt" chưa đủ, phê duyệt phải đúng ticket, còn hạn, đủ hạn mức và đúng người. Nếu không, lòng tin của người duyệt mất, họ kiểm tay 100%, và toàn bộ lợi ích chi phí biến mất dù code vẫn "chạy đúng".

**Một điều còn chưa chắc:**

Trần 800.000đ/ngày, phạm vi 4 kho lẻ và trần 300.000đ/khách/ngày đều tính trên dữ liệu mock của REFUND-v3. Sau 01/12/2026 hạn mức tự động giảm còn 100.000đ, nên tỉ lệ chuyển người và ROI có thể đổi hẳn. Cần đo lại chi phí mỗi ticket, ROI và tỉ lệ kiểm mẫu thật của nhân viên trong pilot trước Bước đánh giá 2.

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