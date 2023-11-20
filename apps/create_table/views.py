from aiohttp import web
from core.settings import db_handler
import json


async def creating_table(request):
    try:
        # Ensure that self.cursor is initialized by connecting to the database
        await db_handler.connect()

        data = await request.json()
        table_name = data.get('table_name')
        columns = data.get('columns')

        if not table_name or not columns:
            return web.Response(text="Invalid request data. 'table_name' and 'columns' are required.", status=400)

        # Create the table if it doesn't exist
        await db_handler.create_table(table_name, columns)

        return web.Response(text="Data table successfully")

    except json.JSONDecodeError:
        return web.Response(text="Invalid JSON in request body.", status=400)

    finally:
        await db_handler.disconnect()

async def inserting_table(request):
    try:
        # # Ensure that self.cursor is initialized by connecting to the database
        await db_handler.connect()

        data = await request.json()
        table_name = data.get('table_name')
        data = data.get('data')

        if not table_name or not data:
            return web.Response(text="Invalid request data. 'table_name' and 'data' are required.", status=400)

        # Create the table if it doesn't exist
        await db_handler.insert_data(table_name, data)

        return web.Response(text="Data table successfully")

    except json.JSONDecodeError:
        return web.Response(text="Invalid JSON in request body.", status=400)

    finally:
        await db_handler.disconnect()


async def index(request):
    return web.Response(text="Hello World!")

async def handle(request):
    name = request.match_info.get('name', "Anonymous")
    text = "Hello, " + name
    return web.Response(text=text)

__all__ = [ 'index', 'handle','creating_table','inserting_table',]