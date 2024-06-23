from app.user.view import user
from app.waste.view import waste
# 定义路由列表
routers = [
    {'route': user, 'prefix': "/itf/lms/user", 'tags': ["用户管理"]},
    {'route': waste, 'prefix': "/itf/lms/wasteType", 'tags': ["垃圾管理"]},
]