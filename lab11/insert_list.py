import psycopg2
from config import *

def insert_list(user_list):
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )
        connection.autocommit = True

        with connection.cursor() as cursor:
            # Construct the SQL query dynamically
            sql = "INSERT INTO users (first_name, second_name, number_phone) IF NOT EXISTS VALUES "
            values = []

            for user in user_list:
                values.append("(%s, %s, %s)")
            sql += ", ".join(values)

            # Execute the query
            cursor.execute(sql, [user.values() for user in user_list])

    except Exception as ex:
        print('[INFO] Error:', ex)

