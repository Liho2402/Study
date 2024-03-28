import re

txt = input()

x = re.split(r'(?<=[a-z])(?=[A-Z])', txt)

print(x)

