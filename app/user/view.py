from fastapi import APIRouter, Query, status,Depends
from typing import Union
from app.user.serialize import UserForm
from app.user.models import Users
from app.common.response import common_response
from utils.encrypt import encryptStr, decryptStr,keyValue
from aioredis import Redis
from db.redis import sys_cache
from utils.jwt import create_access_token
# 实例化APIRouter实例
userrouter = APIRouter()


# 注册具体方法
@userrouter.post("/login")
async def login(login: UserForm, cache: Redis = Depends(sys_cache)):
    password = decryptStr(login.email, login.password)
    newPassword = encryptStr(keyValue, password)
    user = await Users.filter(is_deleted = 0, email = login.email, password = newPassword).first().values('id', 'email', 'uuid','updated_at','created_at', 'roles__id', 'menus__id', 'buttons__id', 'routers__id')
    if user is None:
        return common_response(10000000)
     # 查询token是否存在
    token = await cache.get(name=login.email)
    data = user
    if token is None:
        # 生成token 设置token
        createToken = create_access_token(login.email)
        await cache.set(name=login.email, value=createToken)
        data['token'] = createToken
    else:
       data['token'] = token
    return common_response(200, data)


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
    print("口萨达s萨是谁")
    return common_response(200);