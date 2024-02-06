from math import *

def trapezoid(a, b, h):
    return (1/2) * (a + b) * h

h = int(input("Height:"))
a = int(input("Base, first value: "))
b = int(input("Base, second value:"))

print("Expected Output: ", trapezoid(a, b, h))
