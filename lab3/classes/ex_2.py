class Shape:
    def __init__(self, length):
        self.lengt = length


    def area(self):
        return self.lengt * self.lengt
    

class Square(Shape):
    def __init__(self, length):
        super().__init__(length)

x = Square(int(input()))
print(x.area())