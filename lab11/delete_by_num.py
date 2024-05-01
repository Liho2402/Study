import psycopg2
from config import *

def delete_data_by_username_or_phone(first, phone):

    sql = """DELETE FROM users WHERE first_name = %s OR second_name = %s;"""

    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )
        connection.autocommit = True

        with connection.cursor() as cursor:
            cursor.execute(sql, (first, phone))
            print(f'Delete {cursor.rowcount} rows')
    except Exception as ex:
        print('[INFO] Error:', ex)
