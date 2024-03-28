import re

name = input()

x = re.sub('_','', name.title())

print(x)

