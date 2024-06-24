from fastapi import APIRouter, Query, status
from typing import Union
from app.waste.serialize import Item
from common import response

# 实例化APIRouter实例
wasterouter = APIRouter()


# 注册具体方法
@wasterouter.get("/", status_code=status.HTTP_200_OK)
async def getWasteTypeList(username: Union[str, None] = Query(default=None, min_length=3, max_length=50),
                password: Union[str, None] = Query(default=None, min_length=8, max_length=16)):
    return response.response(data={'detail': "重复"}, code=400)


@wasterouter.post("/", status_code=status.HTTP_200_OK)
async def postWasteTypeItem(user: Item):
    return response.response(data={'detail': "提交wastetype数据"}, code=500, msg="asdad")


@wasterouter.put("/uuid/{uuid}", status_code=status.HTTP_200_OK)
async def putWasteTypeItem(user: Item):
    return response.response(data={'detail': "修改wastetype数据"}, code=500, msg="asdad")

@wasterouter.delete("/uuid/{uuid}", status_code=status.HTTP_200_OK)
async def deleteWasteTypeItem(user: Item):
    return response.response(data={'detail': "删除wastetype数据"}, code=500, msg="asdad")

@wasterouter.get("{uuid}", status_code=status.HTTP_200_OK)
async def getWasteTypeDetail(user: Item):
    return response.response(data={'detail': "删除wastetype数据"}, code=500, msg="asdad")