import psycopg2
from config import *


def sort(column, pattern):
    sql = f"""
            SELECT {column}
            FROM users 
            WHERE {column} LIKE {pattern};"""
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )
        connection.autocommit = True

        with connection.cursor() as cursor:
            cursor.execute(sql)
            rows = cursor.fetchall()
            for row in rows:
                print(row)

    except Exception as ex:
        print('[INFO] Error:', ex)

