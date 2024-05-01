import psycopg2
from config import *
def delete(id):
    rows_deleted = 0
    sql = """DELETE FROM users WHERE id=%s"""
    try:
        connection = psycopg2.connect(
            host = host,
            user=user,
            password=password,
            database=db_name
        )
        with connection.cursor() as cursor:
            cursor.execute(sql, id)
            rows_deleted = cursor.rowcount
            print(f'[INFO] Row with id = {id} was deleted')
    except Exception as _ex:
        print('[INFO] Error', _ex)