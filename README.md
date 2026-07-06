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

## Repositories
Tại đây, ta cần 1 class: TodoRepository

theo yc đề thì sẽ tương ứng cần các hàm xử lí sau:
+ created
+ get_all
+ get_by_id
+ update
+ delete
+ toggle_completd
+ search

Repository không xử lí http,nó cũng không quyết định lỗi. nó chỉ nhận yc từ Service và thao tác với database mà thôi

## Exceptions (Helper)
Tạo helper để trả lỗi HTTP

Tại đây ta tạo 2 function ứng 2 lỗi 404 và 400

+ 404: khi todo không tồn tại -> Function: not_found_exception
+ 400: khi request không hợp lệ về mặt logic -> bad_request_exception

## Services
Nơi thực hiện business logic 

Ta cần tạo 1 class: TodoService

Các method ứng yc:
+ create todo --> get_todo_by_id --> ...
+ get todo ---> seach/getall ----nếu_rỗng--->400
+ get_todo_by_id -> gọi repository get_by_id -----nếu_không_có_todo---> 404
+ update_todo ---> get_todo_by_id -->...
+ delete_todo ---> get_todo_by_id --> ..

## Router
Tạo các endpoint chính cho todo. Router là nơi chỉ nhận path tham số, query (nhận chứ không viết query database), nhận reuqest, gọi service, trả response thôi.

prefix: /todos

dependency: get_to_service

các endpoint:
+ GET /todos
+ GET /todos/{todo_id}
+ POST /todos
+ PUT /todos/{todo_id}
+ DELETE /todos/{todo_id}
+ ...