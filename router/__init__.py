from app.user.view import userrouter
from app.wasteType.view import wasterouter
from app.truck.view import  truckrouter
from app.contractor.view import contractorrouter
from app.user.view import userrouter


# 定义路由列表
routers = [
    {'route': truckrouter, 'prefix': "/itf/lms/web", 'tags': ["车辆管理"]},
    {'route': contractorrouter, 'prefix': "/itf/lms/web", 'tags': ["承包商管理"]},
    {'route': userrouter, 'prefix': "/itf/lms/web", 'tags': ["用户管理"]},
]