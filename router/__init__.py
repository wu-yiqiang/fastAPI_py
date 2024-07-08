from app.user.view import userrouter
from app.wasteType.view import wasterouter
from app.truck.view import  truckrouter
from app.contractor.view import contractorrouter
# 定义路由列表
routers = [
    # {'route': userrouter, 'prefix': "/itf/lms/user", 'tags': ["用户管理"]},
    # {'route': wasterouter, 'prefix': "/itf/lms/wasteType", 'tags': ["垃圾管理"]},
    {'route': truckrouter, 'prefix': "/itf/lms/web", 'tags': ["车辆管理"]},
    {'route': contractorrouter, 'prefix': "/itf/lms/web", 'tags': ["承包商管理"]},
]