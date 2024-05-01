import psycopg2
from config import *

def high():
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )
        connection.autocommit = True

        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT user_name, MAX(score) 
                FROM snake 
                GROUP BY user_name
                LIMIT 1;""")

            row = cursor.fetchone()

            return row

    except Exception as _ex:
        print('[INFO] Error', _ex)
