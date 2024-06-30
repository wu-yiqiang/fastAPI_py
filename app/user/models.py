from tortoise import fields
from tortoise.models import Model

from app.common.db import BaseModel

class User(Model, BaseModel):
    email = fields.CharField(max_length=255, unique=True)
    password = fields.CharField(max_length=255)

    class Meta:
        table = 'user'

class Teacher(Model, BaseModel):
    name = fields.CharField(max_length=255, unique=True)
    gender = fields.BooleanField(max_length=255, null=False)
    teacher_id = fields.IntField(null=False)

    class Meta:
        table = 'teacher'


class Course(Model, BaseModel):
    name = fields.CharField(max_length=255, unique=True)
    password = fields.CharField(max_length=255)
    course_id = fields.IntField(null=False)
    class Meta:
        table = 'course'