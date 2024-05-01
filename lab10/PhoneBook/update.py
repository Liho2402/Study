import psycopg2
from config import *

def update(user_first_name, user_second_name,user_phone, id):
    updated_row_count = 0
    sql = """   UPDATE users
                SET first_name = %s, second_name = %s, number_phone = %s 
                WHERE id = %s"""

    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )
        connection.autocommit = True

        with connection.cursor() as cursor:
            cursor.execute(sql, (user_first_name, user_second_name, user_phone, id))
            updated_row_count = cursor.rowcount
            print('[INFO] Data was updated')
    except Exception as _ex:
        print('[INFO] Error', _ex)
    finally:
        if connection:
            connection.close()
            print('[INFO] Connection closed')
            return updated_row_count