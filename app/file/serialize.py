from pydantic import BaseModel,Field,validator
class PostFileIn(BaseModel):
    filename: str = Field(default="filename")