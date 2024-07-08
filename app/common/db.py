from datetime import datetime
from tortoise import fields
from tortoise.models import Model

class BaseModel(Model):
    uuid: str = fields.UUIDField(pk=True)
    created_at: datetime = fields.DatetimeField(auto_now_add=True)
    updated_at: datetime = fields.DatetimeField(auto_now=True)
    is_deleted: bool = fields.BooleanField(default=False)
    class Meta:
        abstract = True
