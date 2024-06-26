from fastapi import APIRouter, Query, status
from typing import Union
from common import response
from app.user.serialize import Register

# 实例化APIRouter实例
userrouter = APIRouter()


# 注册具体方法
@userrouter.get("/login")
async def login(email: Union[str, None] = Query(default=None, min_length=3, max_length=50),
                password: Union[str, None] = Query(default=None, min_length=8, max_length=16)):
    return response.response(data={'detail': "重复"}, code=400)


@userrouter.post("/register", status_code=status.HTTP_200_OK)
async def register(user: Register):
    return response.response(data={'detail': "账号不能重复"}, code=500, msg="asdad")


@userrouter.post("/userInfo")
async def userInfo():
    return {
        "code": 200,
        "msg": "Hello World!"
    }


@userrouter.post("/changePassword")
async def changePassword():
    return {
        "code": 200,
        "msg": "Hello World!"
    }