from fastapi.encoders import jsonable_encoder
status = {
    200: '操作成功',
    300: '重定向',
    400: '业务错误',
    500: '服务错误',
    10000000: '用户密码错误',
    10000001: '用户不存在',
}

def response(data, code= 200, msg=None):
    print("msg", msg)
    data = {
        'code': code,
        'data': data,
        'msg': msg,
    }
    if msg:
        data['msg'] = msg
    else:
        data['msg'] = status[code]

    return jsonable_encoder(data)