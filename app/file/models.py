from tortoise import fields
from tortoise.models import Model

from app.common.db import BaseModel

class File(BaseModel):
    fileHash = fields.CharField(max_length=255, unique=True)
    filename = fields.CharField(max_length=255, unique=True)
    size = fields.IntField() # 单位为byte
    type = fields.CharField(max_length=255)
    addr = fields.CharField(max_length=65535)

    class Meta:
        table = 'file'