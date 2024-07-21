from fastapi import APIRouter, Query, status
from typing import Union
from common import response
from app.user.serialize import UserForm
from app.user.models import Users
from app.common.response import common_response
from utils.encrypt import encryptStr, decryptStr,keyValue
# 实例化APIRouter实例
userrouter = APIRouter()


# 注册具体方法
@userrouter.post("/login")
async def login(login: UserForm):
    user = await Users.filter(is_deleted = 0, email = login.email, password = login.password).first().values('id', 'email', 'uuid','updated_at','created_at', 'roles__id', 'menus__id', 'buttons__id', 'routers__id')
    if user is None:
        return common_response(10000000)
    # 生成token 设置token
    return common_response(200, user)


@userrouter.post("/register", status_code=status.HTTP_200_OK)
async def register(register: UserForm):
    password = decryptStr(register.email, register.password)
    newPassword = encryptStr(keyValue, password)
    await Users(email=register.email, password=newPassword, is_deleted= 0).save()
    return common_response(200)


@userrouter.post("/userInfo")
async def userInfo(userform: UserForm):
    user = await Users.filter(is_deleted=0, email=userform.email, password=userform.password).first().values('id', 'email','uuid','updated_at','created_at','roles__id','menus__id','buttons__id','routers__id')
    if user is None:
        return common_response(10000000)
    return common_response(200, user)


@userrouter.post("/changePassword")
async def changePassword():
    return {
        "code": 200,
        "msg": "Hello World!"
    }