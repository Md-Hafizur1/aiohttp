from aiohttp import web
from core.routers import *

if __name__ == '__main__':
    app_instance = create_app()
    web.run_app(app_instance)