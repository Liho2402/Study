import psycopg2
from config import *

def file_insert(file_name):
    with open(file_name, 'r') as file:
        for line in file:
            key, value = line.strip().split(': ')

            if key == 'Name':
                name = value
            elif key == 'Secondname':
                second_name = value
            elif key == 'Phone':
                phone_number = value
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
                f"""INSERT INTO users(first_name, second_name, number_phone) VALUES
                (%s, %s, %s);""", (name, second_name, phone_number)
            )
            print('[INFO] Data was added')
    except Exception as _ex:
        print('[INFO] Error', _ex)
    finally:
        if connection:
            connection.close()
            print('[INFO] Connection closed')