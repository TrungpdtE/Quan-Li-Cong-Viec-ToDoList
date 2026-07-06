"""TODO list API
Điểm khởi động của ứng dụng FastAPI.
"""

from fastapi import FastAPI
from app.core.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Todo List API",
    description="Ứng dụng Todo List nhỏ dùng FastAPI, SQLAlchemy ORM và SQLite.",
    version="1.0.0",
)
