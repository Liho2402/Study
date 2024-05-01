import psycopg2
from config import *


def create():
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )
        connection.autocommit = True

        with connection.cursor() as cursor:
            cursor.execute(
                """CREATE TABLE IF NOT EXISTS snake(
                id serial PRIMARY KEY,
                user_name varchar(50) NOT NULL,
                score INT NOT NULL);"""
            )

            print("[INFO] Table created successfully")
    except Exception as _ex:
        print('[INFO] Error', _ex)
    finally:
        if connection:
            connection.close()
            print('[INFO] Connection closed')