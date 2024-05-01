import psycopg2
from config import *


def query_with_pagination(table_name, columns, limit, offset):
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )
        connection.autocommit = True

        with connection.cursor() as cursor:
            # Construct the SQL query
            sql = f"SELECT {', '.join(columns)} FROM {table_name} LIMIT %s OFFSET %s;"

            # Execute the query
            cursor.execute(sql, (limit, offset))

            # Fetch and return the results
            rows = cursor.fetchall()
            return rows

    except Exception as ex:
        print('[INFO] Error:', ex)