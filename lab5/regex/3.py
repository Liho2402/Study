import re

txt = input()

x = re.search(r'[a-z]+_a[a-z]+', txt)

if x:
    print(x.group())
else:
    print('Not found')