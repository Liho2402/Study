def square(a, b):
    for i in range(a, b + 1):
        yield  i ** 2


a, b = int(input()), int(input())
number_square = square(a, b)
print("Squares:")
for i in number_square:
    print(i)

