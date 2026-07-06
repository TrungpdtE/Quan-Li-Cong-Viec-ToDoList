from typing import Annotated
from fastapi import APIRouter, Depends, Query, Response, status
from sqlalchemy.orm import Session
from TodoListApp.core.database import get_db
from TodoListApp.repositories.todo_repository import TodoRepository
from TodoListApp.schemas.todo import TodoCreate, TodoResponse, TodoUpdate
from TodoListApp.services.todo_service import TodoService


router=APIRouter(prefix="/todos", tags=["Todos"])

def get_todo_service(db: Annotated[Session, Depends(get_db)]) -> TodoService:
    todo_repository=TodoRepository(db)
    return TodoService(todo_repository)

@router.get("", response_model=list[TodoResponse])
def get_todos(
    service: Annotated[TodoService, Depends(get_todo_service)],
    completed: bool | None=Query(default=None), search: str | None=Query(default=None),
) -> list[TodoResponse]:
    return service.get_todos(completed=completed, search=search)


@router.get("/{todo_id}", response_model=TodoResponse)
def get_todo_by_id(
    todo_id: int, service: Annotated[TodoService, Depends(get_todo_service)],
) -> TodoResponse:
    return service.get_todo_by_id(todo_id)


@router.post("", response_model=TodoResponse, status_code=status.HTTP_201_CREATED)
def create_todo(
    todo_data: TodoCreate, service: Annotated[TodoService, Depends(get_todo_service)],
) -> TodoResponse:
    return service.create_todo(todo_data)


@router.put("/{todo_id}", response_model=TodoResponse)
def update_todo(
    todo_id: int, todo_data: TodoUpdate,
    service: Annotated[TodoService, Depends(get_todo_service)],
) -> TodoResponse:
    return service.update_todo(todo_id, todo_data)


@router.delete("/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(
    todo_id: int, service: Annotated[TodoService, Depends(get_todo_service)],
) -> Response:
    service.delete_todo(todo_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)