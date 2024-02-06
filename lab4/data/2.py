from datetime import *

current_date = datetime.now()

yesterday = current_date - timedelta(days=1)
tomorrow = current_date + timedelta(days=1)


print(yesterday.strftime("%Y-%m-%d"))
print(current_date.strftime("%Y-%m-%d"))
print(tomorrow.strftime("%Y-%m-%d"))
