import re

txt = input()

x = re.sub(r"([A-Z])", r' \1 ', txt)

print(x)