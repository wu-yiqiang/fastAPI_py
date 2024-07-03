from tortoise import fields
from tortoise.models import Model

from app.common.db import BaseModel

class Driver(BaseModel):
    givenName = fields.CharField(max_length=255, unique=True)
    gender = fields.BooleanField(max_length=255, unique=True, verbose_name="性别 1表示男 0 表示女 3表示其他")
    contractorsId = fields.ForeignKeyField(model_name='app.Contractor', related_name='trucks_contractorsId')
    class Meta:
        table = 'driver'