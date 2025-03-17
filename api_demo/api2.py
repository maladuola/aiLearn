import mysql.connector
from db_config import get_db_config
from logger_config import logging

class API2:
    def __init__(self):
        self.db_config = get_db_config()

    def execute(self, user_id):
        with mysql.connector.connect(**self.db_config) as conn:
            with conn.cursor() as cursor:
                logging.info("Executing SQL: SELECT * FROM users WHERE id = %s", user_id)
                cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
                result = cursor.fetchone()
        return result 