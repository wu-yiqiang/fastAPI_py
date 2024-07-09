from tortoise import fields
from tortoise.models import Model

from app.common.db import BaseModel

class Truck(BaseModel):
    displayName = fields.CharField(max_length=255, unique=True)
    contractorsId = fields.ForeignKeyField(model_name='app.Contractor', related_name='contractorsId')

    class Meta:
        table = 'truck'