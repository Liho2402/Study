
def multiply(list):
    mul = 1
    for i in list:
        mul *= i
    print(mul)

n = int(input("Amount of number in list: "))

list = []

for i in range(n):
    num = int(input())
    list.append(num)

multiply(list)