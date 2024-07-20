from fastapi import status
from fastapi.responses import JSONResponse, Response  
from typing import Union

status = {
    200: '操作成功',
    300: '重定向',
    400: '业务错误',
    500: '服务错误',
    10000000: '帐号或密码错误'
}
def common_response(code = 200, data = None) -> Response:
    return {
        'code': code,
        'message': status[code],
        'data': data,
    }