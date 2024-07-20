import uuid

import jinja2
from fastapi import APIRouter, Query, status
from typing import Union,Optional
from app.wasteType.serialize import Item
from app.common.response import common_response
from app.common.serialize import QueryPageRequest
from app.contractor.serialize import PostContractorIn
from app.contractor.models import Contractor
# 实例化APIRouter实例
contractorrouter = APIRouter()



# 分页查询
@contractorrouter.get("/company/page",status_code=status.HTTP_200_OK)
async def getContractorList(pageSize: int, pageNo: int, keyword: Optional[str], type: int):
    offset_num = (pageNo - 1) * pageSize
    list = await Contractor.filter(type=type, is_deleted=0).all().offset(offset_num).limit(pageSize)
    total = await Contractor.filter(type=type, is_deleted=0).all().count()
    pageNo = pageNo
    pageSize = pageSize
    data = dict()
    data['total'] = total
    data['pageNo'] = pageNo
    data['pageSize'] = pageSize
    data['lists'] = list

    return common_response(200, data=data)

# 全量查询
@contractorrouter.get("/company",status_code=status.HTTP_200_OK)
async def getContractorAllList():
    list = await Contractor.filter(is_deleted=0).all()
    return common_response(200,data=list)

# 新增数据
@contractorrouter.post("/company",status_code=status.HTTP_200_OK)
async def postContractorItem(data: PostContractorIn):
    await Contractor(companyName= data.companyName, email= data.email, type=data.type).save()
    return common_response(200,data=None)



# 查询详情
@contractorrouter.get("/company/uuid/{uuid}",status_code=status.HTTP_200_OK)
async def getContractorDetail(uuid: str):
    item = await Contractor.filter(uuid=uuid,is_deleted=0).first()
    return common_response(200,data=item)

# 修改数据
@contractorrouter.put("/company/uuid/{uuid}",status_code=status.HTTP_200_OK)
async def postContractor(uuid,data: PostContractorIn):
    await Contractor.filter(uuid=uuid, is_deleted = 0).update(companyName=data.companyName, email=data.email, type=data.type)
    return common_response(200,data=None)


# 删除数据
@contractorrouter.delete("/company/uuid/{uuid}",status_code=status.HTTP_200_OK)
async def deleteContractor(uuid):
    await Contractor.filter(uuid=uuid).update(is_deleted=1)
    return common_response(200,data=None)

