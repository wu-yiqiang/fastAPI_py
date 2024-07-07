from pydantic import BaseModel,Field
class QueryPageRequest(BaseModel):
    pageSize: int = Field(default=10)
    pageNo: int = Field(default=1)
    keyword: str = Field(default='查询')
