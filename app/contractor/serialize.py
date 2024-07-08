import re

from pydantic import BaseModel,Field,validator
class PostContractorIn(BaseModel):
    companyName: str = Field(default="conpany1")
    email: str = Field(default="wu_yiqiang@outlook.com")
    type: int = Field(default=0)

    # @validator('email')
    # def isEmail(cls, value):
    #     assert re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", value)
    #     return value