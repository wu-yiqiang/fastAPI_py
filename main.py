import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
# from starlette.staticfiles import StaticFiles
from tortoise.contrib.fastapi import register_tortoise
from settings import  TORTOISE_ORM
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.openapi.docs import (
    get_redoc_html,
    get_swagger_ui_html,
    get_swagger_ui_oauth2_redirect_html,
)
from router import routers

# 实例化
app = FastAPI(docs_url=None, redoc_url=None)
app.openapi_version = "3.0.0"
register_tortoise(
    app,
    config=TORTOISE_ORM,
    # generate_schemas=True,#如果数据库为空，则自动生成对应表单,生产环境不要开
    # add_exception_handlers=True,#生产环境不要开，会泄露调试信息
)
app.add_middleware(
    TrustedHostMiddleware,
    allowed_hosts=["*"],
    # CORSMiddleware=CORSMiddleware,
    # allow_origins=["*"],
    # allow_credentials=True,
    # allow_methods=["*"],
    # allow_headers=["*"],
)
app.mount('/statics', StaticFiles(directory='statics'), name='statics')

@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title=app.title + " - Swagger UI",
        oauth2_redirect_url=app.swagger_ui_oauth2_redirect_url,
        swagger_js_url="/statics/swagger/swagger-ui-bundle.js",
        swagger_css_url="/statics/swagger/swagger-ui.css",
    )

@app.get(app.swagger_ui_oauth2_redirect_url, include_in_schema=False)
async def swagger_ui_redirect():
    return get_swagger_ui_oauth2_redirect_html()

@app.get("/redoc", include_in_schema=False)
async def redoc_html():
    return get_redoc_html(
        openapi_url=app.openapi_url,
        title=app.title + " - ReDoc",
        redoc_js_url="/statics/swagger/redoc.standalone.js",
    )


for router in routers:
    app.include_router(router["route"], prefix=router["prefix"], tags=router["tags"])





if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8899, reload=True)