from app.user.view import userrouter
from app.wasteType.view import wasterouter
# 定义路由列表
routers = [
    {'route': userrouter, 'prefix': "/itf/lms/user", 'tags': ["用户管理"]},
    {'route': wasterouter, 'prefix': "/itf/lms/wasteType", 'tags': ["垃圾管理"]},
]