from math import *

def gradus(degree):
    return round(radians(degree), 4)
    

x = int(input("Input degree"))
print("Output radian: ", gradus(x))