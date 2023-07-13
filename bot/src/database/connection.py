from psycopg2 import OperationalError, connect
from bot.src.settings import config


def create_connection(
        db_name=config.POSTGRES_DB,
        db_user=config.POSTGRES_USER,
        db_pwd=config.POSTGRES_PASSWORD,
        db_host=config.DB_HOST,
        db_port=config.DB_PORT,
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