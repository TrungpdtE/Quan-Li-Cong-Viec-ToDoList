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

### Do đề bài yêu cầu làm theo ngôn ngữ và framework thạo nhất, nên em quyết định lựa chọn FastApi Python để hoàn thành kịp hạn nộp. Nếu có thêm thời gian để học và nghiên cứu về spring java thì em sẽ tiến hành.

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

## Main
Là điểm khởi động của app -> start -> SQLAlchemy tạo table
+ check 400
+ Check health 


## TEST

```bash
python3 -m compileall TodoListApp
```

```bash
uvicorn TodoListApp.main:TodoListApp --reload
```

```bash
http://127.0.0.1:8000
```

![Kiểm tra api hoạt động không](ảnh/img1.png)


```bash
http://127.0.0.1:8000/docs
```

![Giao diện](ảnh/img2.png)

--------------------------

Tạo 1 todo mới trước: 

```bash
curl -X POST http://127.0.0.1:8000/todos \
  -H "Content-Type: application/json" \
  -d '{"title":"Nhớ đăng kí môn kĩ năng thực hành chuyên môn","description":"Dăng Kí Môn Học"}'
```

![Thêm todo thành công](ảnh/img4.png)


--------------------------
```bash
curl -X PATCH http://127.0.0.1:8000/todos/1/toggle
```

Sẽ chuyển completed từ false sang true, ngược lại từ true sang false

![toggle thành công](ảnh/img5.png)

--------------------------
TEST thêm:
```bash
curl "http://127.0.0.1:8000/todos"
```
```bash
curl "http://127.0.0.1:8000/todos?completed=true"
```
```bash
curl "http://127.0.0.1:8000/todos?completed=false"
```
```bash
curl --get \
  --data-urlencode "search=kĩ năng thực hành" \
  http://127.0.0.1:8000/todos
```
```bash
curl --get \
  --data-urlencode "search=kĩ năng thực hành" \
  --data "completed=true" \
  http://127.0.0.1:8000/todos
```

![Test nhanh](ảnh/img6.png)

--------------------------
Test lỗi 400 Bad Request

```bash
curl -X POST http://127.0.0.1:8000/todos \
  -H "Content-Type: application/json" \
  -d '{"title":"   ","description":"invalid"}'
```

![Test nhanh](ảnh/img7.png)
--------------------------
Test lỗi 404 Not Found
```bash
curl http://127.0.0.1:8000/todos/999999
```

![Test nhanh](ảnh/img8.png)
--------------------------
API testing

Cài dependencies
```bash
pip install -r requirements.txt
```


Chạy server
```bash
uvicorn app.main:app --reload
```

Base URL
```bash
http://127.0.0.1:8000
```

Swagger UI (dùng này test backend cho dễ)
```bash
http://127.0.0.1:8000/docs
```

Vào docs test:
```bash
GET /
```
![Health check](ảnh/img3.png)

Tạo Todo mới
```bash
POST /todos
```
![Thêm todo mới - 201 tạo thành công](ảnh/img9.png)

Lấy danh sách todo
```bash
GET /todos
```
![Lấy danh sách Todo toàn bộ - 200 OK](ảnh/img10.png)

Lấy chi tiết todo
```bash
GET /todos/1
```
![Lấy chi tiết todo - 200 OK](ảnh/img11.png)

Cập nhật todo
```bash
PUT /todos/1
```
![Đổi title cho id todo 2 - 200 OK](ảnh/img12.png)

Toggle trạng thái completed
```bash
PATCH /todos/1/toggle
```
![Toggle trạng thái completed của id 1 - 200 OK](ảnh/img13.png)

Lọc todo theo completed
```bash
GET /todos?completed=true
```
![Lọc todo theo completed - 200 OK](ảnh/img14.png)

Tìm kiếm todo theo title
```bash
GET /todos?search=title
```
![Tìm kiếm todo theo title: "title" - 200 OK](ảnh/img15.png)

Kết hợp search và completed
```bash
GET /todos?search=title&completed=true
```
![Kết hợp search và completed: "title" và True - 200 OK](ảnh/img16.png)

Test validation title rỗng
```bash
POST /todos
```
![Test validation title rỗng - 400 Bad Request](ảnh/img17.png)

Test todo không tồn tại
```bash
GET /todos/999999
```
![Test todo không tồn tại - 404 Not Found](ảnh/img18.png)

Xóa todo
```bash
DELETE /todos/2
```
![Xóa todo - 204 No Content](ảnh/img19.png)

Kiểm tra lại sau khi xóa
```bash
GET /todos/2
```
![Kiểm tra lại sau khi xóa - 404 Not Found](ảnh/img20.png)

--------------------------