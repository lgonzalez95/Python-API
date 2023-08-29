import os
from dotenv import load_dotenv

env = os.environ.get("ENV", "local")
load_dotenv("envs/" + env + ".env")


class Configuration:
    def __init__(self):
        self.db_host = os.getenv('DB_HOST')
        self.db_port = os.getenv('DB_PORT')
        self.db_user = os.getenv('DB_USER')
        self.db_password = os.getenv('DB_PASSWORD')
        self.db_name = os.getenv('DB_NAME')
        self.base_api_url = os.getenv('BASE_API_URL')


configuration = Configuration()
