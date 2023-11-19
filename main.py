import uvicorn
from fastapi import FastAPI
from router import routers

# 实例化
app = FastAPI()
# 加载路由 
for item in routers:
    app.include_router(item.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)