class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width


    def area(self, length, width):
        return length * width
    

x, y = int(input()), int(input())
p1 = Rectangle(x,y)

print(p1.area(x,y))