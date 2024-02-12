import re

txt = input()

x = re.search(r"a+b*", txt)

if x:
    print(txt)
else:
    print("Do not match")