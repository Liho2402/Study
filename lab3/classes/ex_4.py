from math import *

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print("Coordinates:", self.x, ',', self.y) 

    def move(self, new_x, new_y):
        print("Change position")
        self.new_x = int(input())
        self.new_y = int(input())
        print("Position changed\n",self.new_x,"  " ,self.new_y)

    def distance(self, second_point):
        for_x = second_point.x - self.x
        for_y = second_point.y - self.y
        return round(sqrt(for_x**2 + for_y**2))


x = int(input())
y = int(input())

point_1 = Point(x, y)
point_1.show()

point_1.move(x, y)

print("Write coordinates for 2 point:")
x_2 = int(input())
y_2 = int(input())

point_2 = Point(x_2, y_2)

print("This distance between them:", point_1.distance(point_2))
