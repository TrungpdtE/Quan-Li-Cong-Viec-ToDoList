"""Các helper tạo HTTPException """
from fastapi import HTTPException, status

#404
def not_found_exception(message:str) -> HTTPException:
    return HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=message,
    )

#400
def bad_request_exception(message:str) -> HTTPException:
    return HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=message,
    )
