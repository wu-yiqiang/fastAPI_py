TORTOISE_ORM = {
    'connections': {
        'default': {
            'engine': 'tortoise.backends.mysql',
            'credentials': {
                'host': '127.0.0.1',
                'port': '3306',
                'user': 'root',
                'password': 'root@root',
                'database': 'fastapi',
                'minsize': 1,
                'maxsize': 5,
                'charset': 'utf8mb4',
                "echo": True
            }
        },
    },
    "apps": {
        'app': {
            "models": ['app.user.models',"aerich.models", 'app.truck.models','app.contractor.models', 'app.driver.models', 'app.models.roles', 'app.models.routers', 'app.models.menus', 'app.models.buttons'],
            'default_connection': 'default',
        }
    },
    'use_tz': False,
    'timezone': 'Asia/Shanghai'
}