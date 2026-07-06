"""Cần class TodoRepository
theo yc đề:
created
get_all
get_by_id
update
delete
toggle_completd
search

Repository chỉ chịu trách nhiệm thao tác dữ liệu Todo với database
"""

from sqlalchemy import select
from sqlalchemy.orm import Session
from TodoListApp.models.todo import Todo
from TodoListApp.schemas.todo import TodoCreate,TodoUpdate


class TodoRepository:
    
    def __init__(self,db: Session) -> None:
        self.db=db

    def create(self,todo_data: TodoCreate) -> Todo:
        todo=Todo(**todo_data.model_dump())
        self.db.add(todo)
        self.db.commit()
        self.db.refresh(todo)
        
        return todo

    def get_all(self,completed: bool | None=None) -> list[Todo]:
        statement=select(Todo).order_by(Todo.id.desc())
        if completed is not None:
            statement=statement.where(Todo.completed == completed)
            
        return list(self.db.scalars(statement).all())

    def get_by_id(self,todo_id: int) -> Todo | None:
        
        return self.db.get(Todo,todo_id)

    def update(self,todo: Todo,todo_data: TodoUpdate) -> Todo:
        update_data=todo_data.model_dump(exclude_unset=True)
        for field,value in update_data.items():
            setattr(todo,field,value)

        self.db.commit()
        self.db.refresh(todo)
        
        return todo

    def delete(self,todo: Todo) -> None:
        self.db.delete(todo)
        self.db.commit()

    def toggle_completed(self,todo: Todo) -> Todo:
        todo.completed=not todo.completed
        self.db.commit()
        self.db.refresh(todo)
        
        return todo

    def search(self,keyword: str,completed: bool | None=None) -> list[Todo]:
        statement=(select(Todo).where(Todo.title.ilike(f"%{keyword}%")).order_by(Todo.id.desc()))
        if completed is not None:
            statement=statement.where(Todo.completed == completed)
            
        return list(self.db.scalars(statement).all())
