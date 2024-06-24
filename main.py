import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.staticfiles import StaticFiles

from router import routers

# 实例化
app = FastAPI()
app.mount('/statics', StaticFiles(directory='statics'), name='statics')

for router in routers:
    app.include_router(router["route"], prefix=router["prefix"], tags=router["tags"])


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8899, reload=True)