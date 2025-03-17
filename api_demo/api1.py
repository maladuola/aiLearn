import mysql.connector
from db_config import get_db_config
from logger_config import logging

# 移除重复的日志配置

class API1:
    def __init__(self):
        self.db_config = get_db_config()

    def execute(self):
        with mysql.connector.connect(**self.db_config) as conn:
            with conn.cursor() as cursor:
                logging.info("Executing SQL: SELECT * FROM users")
                cursor.execute("SELECT * FROM users")
                result = cursor.fetchall()
        return result 