import uvicorn
from fastapi import FastAPI
from router import routers
# 实例化
app = FastAPI()


for router in routers:
    app.include_router(router.route, prefix=router.prefix, tags=[router.tag])


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8899, reload=True)