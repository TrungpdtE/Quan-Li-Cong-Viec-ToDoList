# XÂY DỰNG BACKEND CHO QUẢN LÍ CÔNG VIỆC (ToDo List)

Phân tích đề: 

Đề xây dựng một ứng dụng ToDo List có các chức năng:

+ Xem danh sách công việc
+ Xem chi tiết 1 công việc
+ Thêm Công việc
+ Chỉnh sửa công việc
+ Xoá công việc
+ Đánh dấu hoàn thành / chưa hoàn thành
+ Tìm kiếm theo tên title
+ Lọc theo trạng thái hoàn thành 

Dữ liệu chính của hệ thống:

+ id
+ title
+ mô tả (description)
+ trạng thái (completed)
+ thời điểm tạo (created_at)
+ thời điểm sửa/bổ sung (updated_at)

Do đề bài yêu cầu làm theo ngôn ngữ và framework thạo nhất, nên em quyết định lựa chọn FastApi Python để hoàn thành kịp hạn nộp. Nếu có thêm thời gian để học và nghiên cứu về spring java thì em sẽ tiến hành.

Vì FastAPi nên project nên chia thành Router - Service - Repository - Model - Schema theo cấu trúc thông thường.

## Models

ở Model đây là nơi đại diện cho dữ liệu được lưu trong database. nó chưa phải dữ liệu request/response

Todo class gồm các field (đã nói ở dữ liệu chính hệ thống phía trên)
+ id
+ title -> có giới hạn kí tự (50)
+ description -> cho phép null
+ completed -> mặc định là chưa xong (False)
+ created_at
+ updated_at

## Schemas
Tại đây mình cần 3 schema:
+ TodoCreate -> title, description
+ TodoUpdate -> title, description, completd
+ TodoResponse -> trả dữ liệu: id,title,description,completed, created_at, updated_at

không xài schema cho mọi thứ. khi tạo todo, client không phải là kẻ quyết định id, mà đó là do server/app quyết định. server cần trả id, created_at, updated_at. Vì vậy cần tách schema theo mục đichs sử dụng
