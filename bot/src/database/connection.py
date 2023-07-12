from psycopg2 import OperationalError, connect
import os

name = os.environ['POSTGRES_DB']
user = os.environ['POSTGRES_USER']
password = os.environ['POSTGRES_PASSWORD']
host = os.environ['DB_HOST']
port = os.environ['DB_PORT']

def create_connection(
        db_name=name,
        db_user=user,
        db_pwd=password,
        db_host=host,
        db_port=port,
):
    try:
        print('try to connect')
        connection = connect(
            database=db_name, 
            user=db_user, 
            password=db_pwd, 
            host=db_host, 
            port=db_port)
        print('connection is successful')
    except OperationalError as connect_error:
        print(f'error: {connect_error}')
        connection = None
    return connection


conn = create_connection()