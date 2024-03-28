import os

show = os.getcwd()
print(show)
print('\n')
print(f"Exists the path: {os.access(show, os.F_OK)}\n"
      f"Readability: {os.access(show, os.R_OK)}\n"
      f"Writability: {os.access(show, os.W_OK)}\n"
      f"Executability: {os.access(show, os.EX_OK)}")
