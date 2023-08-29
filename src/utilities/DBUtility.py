import pymysql
import logging as logger
from src.config.Configuration import configuration


class DBUtility(object):
    def __init__(self):
        self.db_host = configuration.db_host
        self.db_port = configuration.db_port
        self.db_user = configuration.db_user
        self.db_password = configuration.db_password

    def create_connection(self):
        if self.db_user or self.db_password:
            connection = pymysql.connect(host=self.db_host, user=self.db_user,
                                         password=self.db_password, port=int(self.db_port))
        else:
            raise Exception("The DB credentials 'DB_USER and 'DB_PASSWORD' must be set as ENV variables'")
        return connection

    def execute_select(self, sql):
        connection = self.create_connection()

        try:
            logger.debug(f"Executing: {sql}")
            cursor = connection.cursor()
            cursor.execute(sql)
            results_dict = cursor.fetchall()
            cursor.close()
        except Exception as e:
            raise Exception(f"Failed running sql: {sql} \n  Error: {str(e)}")
        finally:
            connection.close()

        return results_dict
