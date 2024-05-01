import psycopg2
from config import *

def insert_nickname(name, score):

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
                f"""INSERT INTO snake(user_name, score) VALUES
                    (%s, %s);""", (name, score)
                )
            print('[INFO] Data was added')
    except Exception as _ex:
        print('[INFO] Error', _ex)
    finally:
        if connection:
            connection.close()
            print('[INFO] Connection closed')
