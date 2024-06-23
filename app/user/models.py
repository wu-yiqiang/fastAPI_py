from fastapi import APIRouter, Query, status
from typing import Union
from request import user
from common import response

# 实例化APIRouter实例
router = APIRouter(tags=["用户管理"])


# 注册具体方法
@router.get("/login", status_code=status.HTTP_200_OK)
async def login(username: Union[str, None] = Query(default=None, min_length=3, max_length=50),
                password: Union[str, None] = Query(default=None, min_length=8, max_length=16)):
    return response.response(data={'detail': "重复"}, code=400)


@router.post("/register", status_code=status.HTTP_200_OK)
async def register(user: user.Register):
    return response.response(data={'detail': "账号不能重复"}, code=500, msg="asdad")


@router.post("/userInfo")
async def userInfo():
    return {
        "code": 200,
        "msg": "Hello World!"
    }


@router.post("/changePassword")
async def changePassword():
    return {
        "code": 200,
        "msg": "Hello World!"
    }