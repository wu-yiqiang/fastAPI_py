from tortoise import fields
from tortoise.models import Model

from app.common.db import BaseModel


class Menu(BaseModel):
    menu_name = fields.CharField(max_length=255, unique=True)
    class Meta:
        table = 'menu'