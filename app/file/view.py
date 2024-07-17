from fastapi import APIRouter, Query, status
from typing import Union, Optional
from app.common.response import response_success
# from app.file.serialize import PostTruckIn
# 实例化APIRouter实例
filerouter = APIRouter()


# 文件上处
@filerouter.get("/file/upload",status_code=status.HTTP_200_OK)
async def uploadFile(filename: str):
    # offset_num = (pageNo - 1) * pageSize
    # lists = await Truck.filter(is_deleted=0).all().offset(offset_num).limit(pageSize).values('displayName', 'contractors__companyName')
    # total = await Truck.filter(is_deleted=0).all().count()
    # pageNo = pageNo
    # pageSize = pageSize
    # data = dict()
    # data['total'] = total
    # data['pageNo'] = pageNo
    # data['pageSize'] = pageSize
    # data['lists'] = lists
    return response_success(data=[])
