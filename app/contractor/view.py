import jinja2
from fastapi import APIRouter, Query, status
from typing import Union,Optional
from app.wasteType.serialize import Item
from app.common.response import response_success
from app.common.serialize import QueryPageRequest
from app.contractor.serialize import PostContractorIn
from app.contractor.models import Contractor
# 实例化APIRouter实例
contractorrouter = APIRouter()



@contractorrouter.get("/company/page",status_code=status.HTTP_200_OK)
async def getContractorList(pageSize: int, pageNo: int, keyword: Optional[str], type: int):
    offset_num = (pageNo - 1) * pageSize
    list = await Contractor.filter(type=type, is_deleted=0).all().offset(offset_num).limit(pageSize)
    return response_success(data=list)


@contractorrouter.post("/company",status_code=status.HTTP_200_OK)
async def postContractor(data: PostContractorIn):
    await Contractor(companyName= data.companyName, email= data.email, type= data.type).save()
    return response_success(data=None)



@contractorrouter.get("/company/uuid/{uuid}",status_code=status.HTTP_200_OK)
async def getContractorDetail(uuid: str):
    item = await Contractor.filter(uuid=uuid,is_deleted=0).first()
    return response_success(data=item)

@contractorrouter.put("/company/uuid/{uuid}",status_code=status.HTTP_200_OK)
async def postContractor(uuid,data: PostContractorIn):
    await Contractor.filter(uuid=uuid, is_deleted = 0).update(companyName=data.companyName, email=data.email, type=data.type)
    return response_success(data=None)


@contractorrouter.delete("/company/uuid/{uuid}",status_code=status.HTTP_200_OK)
async def deleteContractor(uuid):
    await Contractor.filter(uuid=uuid).update(is_deleted=1)
    return response_success(data=None)

