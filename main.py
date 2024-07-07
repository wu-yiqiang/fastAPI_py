import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.staticfiles import StaticFiles
from tortoise.contrib.fastapi import register_tortoise
from settings import  TORTOISE_ORM
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from router import routers

# 实例化
app = FastAPI(title="FastAPI",
    description="FastAPI接口文档",
    version="1.0.0",)
register_tortoise(
    app,
    config=TORTOISE_ORM,
    # generate_schemas=True,#如果数据库为空，则自动生成对应表单,生产环境不要开
    # add_exception_handlers=True,#生产环境不要开，会泄露调试信息
)
app.add_middleware(
    TrustedHostMiddleware, allowed_hosts=["*"]
)
app.mount('/statics', StaticFiles(directory='statics'), name='statics')

for router in routers:
    app.include_router(router["route"], prefix=router["prefix"], tags=router["tags"])

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8899, reload=True)