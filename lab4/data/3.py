from datetime import *

x = datetime.now()

without_micro = x.replace(microsecond=0)

print(without_micro.strftime("%Y-%M-%d, %H:%M:%S.%f"))