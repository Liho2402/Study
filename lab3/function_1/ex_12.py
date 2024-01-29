def histogtram(*x):
    for i in x:
        print(i * '*')
        
x, y, z = int(input()), int(input()), int(input())
histogtram(x, y, z)