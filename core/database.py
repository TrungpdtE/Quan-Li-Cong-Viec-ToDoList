"""Đây là nơi cấu hình database dùng chung cho toàn app"""
"""Cấu hình kết nối SQLite và session làm việc với database"""

import os
from collections.abc import Generator
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase,Session,sessionmaker

DATABASE_URL=os.getenv("DATABASE_URL", "sqlite:///./todos.db")

engine=create_engine(DATABASE_URL,connect_args={"check_same_thread": False},)
SessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine,)

class Base(DeclarativeBase):
    pass

def get_db() -> Generator[Session, None, None]:
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()
