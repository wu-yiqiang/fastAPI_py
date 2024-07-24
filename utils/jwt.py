import os
from datetime import datetime, timedelta
from typing import Union, Any
from app.user.models import Users
import jwt
from aioredis import Redis
from db.redis import sys_cache
from common.response import response
from fastapi import Depends, FastAPI, HTTPException, status
# from jwt.exceptions import InvalidTokenError
# from jose import jwt
# from jose.exceptions import ExpiredSignatureError,JWEError
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/itf/lms/web/login",
    scheme_name="JWT"
)
ACCESS_TOKEN_EXPIRE_MINUTES = 30  # 30 minutes
REFRESH_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7 # 7 days
ALGORITHM = "HS256"
JWT_SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"   # should be kept secret
JWT_REFRESH_SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"    # should be kept secret


def create_access_token(subject: Union[str, Any], expires_delta: int = None) -> str:
    if expires_delta is not None:
        expires_delta = datetime.utcnow() + expires_delta
    else:
        expires_delta = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode = {"exp": expires_delta, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET_KEY, ALGORITHM)
    return encoded_jwt


def create_refresh_token(subject: Union[str, Any], expires_delta: int = None) -> str:
    if expires_delta is not None:
        expires_delta = datetime.utcnow() + expires_delta
    else:
        expires_delta = datetime.utcnow() + timedelta(minutes=REFRESH_TOKEN_EXPIRE_MINUTES)

    to_encode = {"exp": expires_delta, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, JWT_REFRESH_SECRET_KEY, ALGORITHM)
    return encoded_jwt


# def judgeToken(token):
#     """
#     判断token
#     :param token: token串
#     :return: boolen
#     """
#     try:
#         payload = jwt.decode(token, JWT_SECRET_KEY)
#         # todo check 解密串 ，可以自己写，一般是去查询数据库
#         print("解密串")
#         if payload["username"] == 'chacha' and payload["password"] == '12323':
#             print(payload)
#             return True
#         else:
#             print("token 身份错误")
#             return False
#     except ExpiredSignatureError as e:
#         print("token 过期了,{}".format(str(e)))
#         return False
#     except JWEError as e:
#         print("token 验证失败,{}".format(str(e)))
#         return False
#
# def login_required(token=Depends(oauth2_scheme)):
#     """
#     登录认证token
#     :param token:
#     :return:boolen
#     """
#     credentials_exception = HTTPException(
#         status_code=status.HTTP_411_LENGTH_REQUIRED,
#         detail="Authenticate fail！",
#         headers={"WWW-Authenticate": "Bearer"}
#     )
#     if judgeToken(token):
#         return True
#     else:
#         raise credentials_exception
