from pydantic import BaseModel,Field,validator
class PostTruckIn(BaseModel):
    displayName: str = Field(default="conpany1")
    contractorsId: int = Field(default=1)