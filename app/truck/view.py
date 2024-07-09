from fastapi import APIRouter, Query, status
from typing import Union, Optional
from app.truck.models import Truck
from app.contractor.models import Contractor
from app.common.response import response_success
from app.common.serialize import QueryPageRequest
from app.truck.serialize import PostTruckIn
# 实例化APIRouter实例
truckrouter = APIRouter()


@truckrouter.get("/disposalTruck/page",status_code=status.HTTP_200_OK)
async def getTruckList(pageSize: int, pageNo: int, keyword: Optional[str]):
    offset_num = (pageNo - 1) * pageSize
    lists = await Truck.filter(is_deleted=0).all().offset(offset_num).limit(pageSize).values('displayName', 'contractors__companyName')
    # for list in lists:
    #     list.contractor =
    return response_success(data=lists)

@truckrouter.post("/disposalTruck",status_code=status.HTTP_200_OK)
async def postTruckItem(data: PostTruckIn):
    await Truck(displayName=data.displayName, contractors_id=data.contractorsId).save()
    return response_success(data=None)
