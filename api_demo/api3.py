import mysql.connector
from db_config import get_db_config
from logger_config import logging

# 配置日志
logging.basicConfig(level=logging.INFO)

class API3:
    def __init__(self):
        self.db_config = get_db_config()

    def execute(self, name, email):
        with mysql.connector.connect(**self.db_config) as conn:
            with conn.cursor() as cursor:
                logging.info("Executing SQL: INSERT INTO users (name, email) VALUES (%s, %s)", name, email)
                cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
                conn.commit() 