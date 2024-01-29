from math import *

def volume(x):
    V = round((4/3) * (x * x * x))
    print(f'{V}π')

radius = int(input())
volume(radius) 