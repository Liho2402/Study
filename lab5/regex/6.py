import re

txt = input("Enter ")

x = re.sub(r"[ ,.]", "|", txt)

print(x)