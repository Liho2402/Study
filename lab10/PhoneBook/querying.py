import psycopg2
from config import *

def sort():
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )
        connection.autocommit = True

        with connection.cursor() as cursor:
            cursor.execute("""SELECT id, first_name, number_phone FROM users ORDER BY first_name""")
            print("The number of parts: ", cursor.rowcount)
            row = cursor.fetchone()

            while row is not None:
                print(row)
                row = cursor.fetchone()
    except Exception as _ex:
        print('[INFO] Error', _ex)