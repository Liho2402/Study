import psycopg2
from config import *

try:
    connection = psycopg2.connect(
        host = host,
        user=user,
        password=password,
        database=db_name
    )
    connection.autocommit = True

    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT version();"
        )
        print(f'Server version:{cursor.fetchone()}')

#    create table

    with connection.cursor() as cursor:
        cursor.execute(
            """CREATE TABLE users(
            id serial PRIMARY KEY,
            first_name varchar(50) NOT NULL,
            second_name varchar(50) NOT NULL,
            number_phone varchar(20) NOT NULL);"""
        )

        print("[INFO] Table created successfully")
except Exception as _ex:
    print('[INFO] Error', _ex)
finally:
    if connection:
        connection.close()
        print('[INFO] Connection closed')
