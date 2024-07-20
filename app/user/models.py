from tortoise import fields
from tortoise.models import Model

from app.common.db import BaseModel

class Users(BaseModel):
    email = fields.CharField(max_length=255, unique=True)
    password = fields.CharField(max_length=255)
    roles = fields.ManyToManyField(model_name='app.Roles', related_name='user_role')
    menus = fields.ManyToManyField(model_name='app.Menus', related_name='user_menu')
    buttons = fields.ManyToManyField(model_name='app.Buttons', related_name='user_button')
    routers = fields.ManyToManyField(model_name='app.Routers', related_name='user_router')
    class Meta:
        table = 'users'