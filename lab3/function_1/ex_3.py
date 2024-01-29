def solve(numheads, numlegs):
    x = numlegs - numheads * 2
    print(f'Chicken: {x / 2} \nRabbit {numheads - x / 2}')


x = int(input())
y = int(input())
solve(x, y)