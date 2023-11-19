from fastapi import APIRouter
# 实例化APIRouter实例
router = APIRouter(tags=["用户管理"])
# 注册具体方法
@router.get("/login")
async def login():
    """
    默认访问链接
    """
    return {
        "code": 200,
        "msg": "Hello World!"
    }


@router.post("/register")
async def register():
    """
    默认访问链接
    """
    return {
        "code": 200,
        "msg": "Hello World!"
    }

@router.post("/changePassword")
async def changePassword():
    """
    默认访问链接
    """
    return {
        "code": 200,
        "msg": "Hello World!"
    }