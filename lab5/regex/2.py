import re

txt = input()

x = re.search(r'a+b{2,3}', txt)

if x:
    print(txt)
else:
    print("Does not match")