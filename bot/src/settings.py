import logging
import os
from dotenv import load_dotenv

logging.basicConfig(format="%(levelname)s:%(message)s", level=logging.WARNING)
load_dotenv()


class Config():
    def __init__(self) -> None:
        self.BOT_TOKEN = self._check_env('BOT_TOKEN')
        self.BOT_NAME = self._check_env('BOT_NAME')
        self.BOT_USER_NAME = self._check_env('BOT_USER_NAME')
        self.POSTGRES_PASSWORD = self._check_env('POSTGRES_PASSWORD')
        self.POSTGRES_USER = self._check_env('POSTGRES_USER')
        self.POSTGRES_DB = self._check_env('POSTGRES_DB')
        self.DB_HOST = self._check_env('DB_HOST')
        self.DB_PORT = self._check_env('DB_PORT')
        self.PGADMIN_DEFAULT_EMAIL = self._check_env('PGADMIN_DEFAULT_EMAIL')
        self.PGADMIN_DEFAULT_PASSWORD = self._check_env('PGADMIN_DEFAULT_PASSWORD')

    def _check_env(self, env_name):
        try:
            attr_value = os.environ[env_name]
            return attr_value
        except KeyError as env_error:
            logging.critical(f"Can't read from enviroment variable. Message: {env_error}")
            raise KeyError(env_error)
        
config = Config()