import psycopg2
from config import *
from update import update
from querying import sort
from file_insert import file_insert
from delete import delete
def insert():
    name = input('Enter your name: ')
    secondname = input('Enter your second name: ')
    phone = input('Enter your phone: ')

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
                (%s, %s, %s);""", (name, secondname, phone)
            )
            print('[INFO] Data was added')
    except Exception as _ex:
        print('[INFO] Error', _ex)
    finally:
        if connection:
            connection.close()
            print('[INFO] Connection closed')


done = False
while not done:
    variable = input('Do you  want add information? y or n or q? ')
    if variable == 'y':
        variable = input("Insert information from file ? y or n ?")
        if variable == 'y':
            file_name = input("Write file name: ")
            file_insert(file_name)
        else:
            insert()

    elif variable == 'n':
        variable = input('Do you want change information ? y or n ? ')
        if variable == 'y':
            variable = input('Do you want delete information ? y or n ? ')
            if variable == 'y':
                user_id = input('Write id: ')
                delete(user_id)
            else:
                user_id = input("Insert id of user: ")
                name = input("Write new name: ")
                second = input('Write new secondname: ')
                phone = input('Write new phone ')
                update(name, second, phone, user_id)

        elif variable == 'n':
            variable = input('Do you want filter information ? y or n ? ')
            if variable == 'y':
                sort()
    else:
        print('Okay')
        done = True