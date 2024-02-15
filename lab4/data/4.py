from datetime import *

def seconds(x, y):
    x_date = datetime(year = x[0], month = x[1], day = x[2])
    y_date = datetime(year = y[0], month = y[1], day = y[2])

    if x_date > y_date:
        print((x_date-y_date).total_seconds())
    else:
        print((y_date-x_date).total_seconds())

first_date = input("Enter first date time in format yyyy-mm-dd: ").split("-")
second_date = input("Enter second date time in format yyyy-mm-dd: ").split("-")


seconds(list(map(int, first_date)), list(map(int, second_date)))