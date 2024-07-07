from fastapi import APIRouter, Query, status
from typing import Union
from app.wasteType.serialize import Item
from app.common.response import response_success
from app.common.serialize import QueryPageRequest

# 实例化APIRouter实例
truckrouter = APIRouter()


# 注册具体方法
@truckrouter.get("/disposalTruck/page",status_code=status.HTTP_200_OK)
async def getWasteTypeList(data: QueryPageRequest):
    # print(data)
    return response_success(data="asdas")
