import psycopg2
from config import *


def new_phone(first, second, number_phone):
    sql = """
            UPDATE users
            SET number_phone = %s 
            WHERE first_name = %s AND second_name = %s;"""
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )
        connection.autocommit = True

        with connection.cursor() as cursor:
            cursor.execute(sql, (number_phone, first, second))

    except Exception as ex:
        print('[INFO] Error:', ex)

