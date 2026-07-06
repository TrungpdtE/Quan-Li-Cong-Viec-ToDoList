"""Service chứa business logic của Todo List."""

from TodoListApp.exceptions.http_exception import bad_request_exception,not_found_exception
from TodoListApp.models.todo import Todo
from TodoListApp.repositories.todo_repository import TodoRepository
from TodoListApp.schemas.todo import TodoCreate,TodoUpdate


class TodoService:
    def __init__(self,todo_repository: TodoRepository) -> None:
        self.todo_repository=todo_repository

    def create_todo(self,todo_data: TodoCreate) -> Todo:
        return self.todo_repository.create(todo_data)

    def get_todos(self,completed:bool | None=None,search: str | None=None,) -> list[Todo]:
        if search is not None:
            keyword=search.strip()
            if not keyword:
                raise bad_request_exception("Không để trống")
            
            return self.todo_repository.search(keyword,completed)

        return self.todo_repository.get_all(completed)

    def get_todo_by_id(self,todo_id: int) -> Todo:
        todo=self.todo_repository.get_by_id(todo_id)
        if todo is None:
            raise not_found_exception("Todo không tồn tại")
        
        return todo

    def update_todo(self,todo_id: int,todo_data: TodoUpdate) -> Todo:
        todo=self.get_todo_by_id(todo_id)
        
        return self.todo_repository.update(todo,todo_data)

    def delete_todo(self,todo_id: int) -> None:
        todo=self.get_todo_by_id(todo_id)
        
        self.todo_repository.delete(todo)

    def toggle_todo_completed(self,todo_id: int) -> Todo:
        todo=self.get_todo_by_id(todo_id)
        
        return self.todo_repository.toggle_completed(todo)
