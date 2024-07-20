from tortoise import fields
from tortoise.models import Model

from app.common.db import BaseModel

class User(BaseModel):
    email = fields.CharField(max_length=255, unique=True)
    password = fields.CharField(max_length=255)
    roles_id = fields.ManyToManyField()
    # menus = fields.CharField(max_length=255)
    # routers = fields.CharField(max_length=255)

    class Meta:
        table = 'user'