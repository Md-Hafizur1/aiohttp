from aiohttp import web
from apps.create_table.routers import *

def create_app():
    return app

__all__ = ['create_app']