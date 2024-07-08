from tortoise import fields
from tortoise.models import Model

from app.common.db import BaseModel

class Contractor(BaseModel):
    companyName = fields.CharField(max_length=255, unique=True)
    email = fields.CharField(max_length=255)
    type = fields.IntField(max_length=1)
    class Meta:
        table = 'contractor'