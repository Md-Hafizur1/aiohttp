import aiohttp
from aiohttp import web
import psycopg2

class DatabaseHandler:
    def __init__(self, connection_params):
        self.connection_params = connection_params
        self.connection = None
        self.cursor = None

    async def connect(self):
        self.connection = psycopg2.connect(**self.connection_params)
        self.cursor = self.connection.cursor()

    async def disconnect(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()

    async def create_table(self, table_name, columns):
        create_table_query = f"""
            CREATE TABLE IF NOT EXISTS {table_name} (
                {', '.join(columns)}
            );
        """
        self.cursor.execute(create_table_query)
        self.connection.commit()


    async def insert_data(self, table_name, data):
        column_names = ', '.join(data.keys())
        value_placeholders = ', '.join('%s' for _ in range(len(data)))
        insert_query = f"""
            INSERT INTO {table_name} ({column_names})
            VALUES ({value_placeholders});
        """

        self.cursor.execute(insert_query, tuple(data.values()))
        self.connection.commit()

    async def run_query(self, query, params=None):
        def _execute():
            self.cursor.execute(query, params)
            self.connection.commit()

        await self.loop.run_in_executor(None, _execute)

__all__ = ['DatabaseHandler']