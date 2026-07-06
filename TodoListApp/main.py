"""TODO list API Điểm khởi động của ứng dụng FastAPI.
"""

from fastapi import FastAPI, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from app.core.database import Base, engine
from app.routers.todo_router import router as todo_router


Base.metadata.create_all(bind=engine)

app=FastAPI(
    title="Todo List API",
    description="Ứng dụng Todo List",
    version="1.0.0",
)

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(
    request: Request,
    exc: RequestValidationError,
) -> JSONResponse:
    """Trả lỗi validation 400"""
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={
            "message": "Invalid request data",
            "detail": jsonable_encoder(exc.errors()),
        },
    )

@app.get("/")
def health_check() -> dict[str, str]:
    return {"message": "Todo List API đang chạy"}

app.include_router(todo_router)