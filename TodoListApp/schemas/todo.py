"""mục tiêu:
TodoCreate
+ 
TodoUpdate
TodoResponse
"""

"""File: app/schemas/todo.py

Pydantic DTO dùng để nhận request và trả response.
"""

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, field_validator


class TodoResponse(BaseModel):
    id: int
    title: str
    description: str | None
    completed: bool
    created_at: datetime
    updated_at: datetime
    model_config=ConfigDict(from_attributes=True)

class TodoCreate(BaseModel):
    
    title: str=Field(..., min_length=1,max_length=100)
    description: str | None=Field(default=None,max_length=500)

    @field_validator("title")
    @classmethod
    def validate_title(cls, value: str) -> str:
        title=value.strip()
        if not title:
            raise ValueError("Title không được để trống")
        
        return title

    @field_validator("description")
    @classmethod
    def validate_description(cls, value: str | None) -> str | None:
        if value is None:
            return value
        description=value.strip()
        
        return description or None


class TodoUpdate(BaseModel):
    title: str | None=Field(default=None, min_length=1, max_length=100)
    description: str | None=Field(default=None, max_length=500)
    completed: bool | None=None

    @field_validator("title")
    @classmethod
    def validate_title(cls, value: str | None) -> str | None:
        if value is None:
            return value
        title=value.strip()
        if not title:
            raise ValueError("Title không được để trống")
        return title

    @field_validator("description")
    @classmethod
    def validate_description(cls, value: str | None) -> str | None:
        if value is None:
            return value
        description=value.strip()
        
        return description or None

