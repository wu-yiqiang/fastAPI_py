from fastapi import status
from fastapi.responses import JSONResponse, Response  
from typing import Union
def response_success(*, data: Union[list, dict, str]) -> Response:
    return {
        'code': 200,
        'message': "Success",
        'data': data,
    }
def response_error(*, data: str = None, message: str="BAD REQUEST") -> Response:
    return {
        'code': 400,
        'message': message,
        'data': data,
    }