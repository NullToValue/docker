from .connection import conn
from psycopg2 import OperationalError


def execute_query(query, connection=conn):
    connection.autocommit = True
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print('query executed succsse')
    except OperationalError as query_error:
        print(f"error during execute: {query_error}")


create_message_table = """
CREATE TABLE IF NOT EXISTS message (
    id SERIAL PRIMARY KEY,
    message_text TEXT,
    user_id INTEGER NOT NULL,
    message_time TIMESTAMP WITH TIME ZONE
)
"""   


execute_query(create_message_table)