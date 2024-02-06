from datetime import *
from time import sleep

x = datetime.now()

x_tomorrow = x + timedelta(seconds=50)

print((x_tomorrow - x).seconds)