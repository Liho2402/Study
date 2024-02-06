from datetime import *

x = datetime.now()

current_date = x - timedelta(days=5)

print(current_date.strftime("%Y-%m-%d"))