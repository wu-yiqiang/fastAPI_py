from pydantic import BaseModel
class UserForm(BaseModel):
    email: str = 'sutter.wu@itforce-tech.com'
    password: str = 'DSq10PttORQFdMRVdrN+5Q=='



class PostUserIn(BaseModel):
    email: str = 'sutter.wu@itforce-tech.com'
    password: str = 'DSq10PttORQFdMRVdrN+5Q=='
    name: str = 'asdsad'
    picture: str = '阿松大'