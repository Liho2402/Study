from math import *

def polligon_area(number_of_sides, length_of_side):
    apothem = length_of_side / (2 * tan(pi / number_of_sides))
    return round((length_of_side * number_of_sides * apothem) / 2)


n = int(input("Input number of sides: "))

if n > 2:
    l = int(input("Input the length of a side: "))
    print("The area of the polygon is: ", polligon_area(n, l))
else:
    print("Polygon does not exist")