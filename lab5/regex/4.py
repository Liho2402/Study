import re

txt = input("Enter a string: ")
x = re.search(r"[A-Z][a-z]+", txt)

if x:
    print(x.group())
else:
    print("Not found")