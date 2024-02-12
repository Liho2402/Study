import re


txt = input('Write your string: ')

x = re.search(r'a[a-z]*b', txt)

if x:
    print(x.group())
else:
    print('Not found')