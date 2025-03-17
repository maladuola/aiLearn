import mysql.connector
from db_config import get_db_config
from logger_config import logging

# 配置日志
logging.basicConfig(level=logging.INFO)

class API4:
    def __init__(self):
        self.db_config = get_db_config()

    def execute(self, user_id, new_email):
        with mysql.connector.connect(**self.db_config) as conn:
            with conn.cursor() as cursor:
                logging.info("Executing SQL: UPDATE users SET email = %s WHERE id = %s", new_email, user_id)
                cursor.execute("UPDATE users SET email = %s WHERE id = %s", (new_email, user_id))
                conn.commit() 