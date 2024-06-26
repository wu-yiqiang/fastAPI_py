from tortoise import fields
from tortoise.models import Model

from app.common.db import BaseModel

class User(BaseModel):
    email = fields.CharField(max_length=255, unique=True)
    password = fields.CharField(max_length=255)

    class Meta:
        table = 'user'