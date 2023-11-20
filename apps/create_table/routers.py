from aiohttp import web
from apps.create_table.views import *
from core.settings import *

app.add_routes([web.get('/', handle),
                web.get('/{name}', handle),
                web.post('/create_table', creating_table),
                web.post('/insert_table', inserting_table),
            ])

__all__ = ['app']