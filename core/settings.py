from aiohttp import web
from core.db import *
app = web.Application()

connection_params = {
    'dbname': 'test',
    'user': 'postgres',
    'password': 'hafizur1979',
    'host': '127.0.0.1',
    'port': '5432',
}
# Create an instance of DatabaseHandler with connection parameters
db_handler = DatabaseHandler(connection_params)

__all__ = ['app', 'db_handler']