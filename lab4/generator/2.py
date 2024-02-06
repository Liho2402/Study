def gen_even(n):
    for i in range(0, n + 1):
        if i % 2 == 0:
            yield i
    

n = int(input())
even_numbers = gen_even(n)

print("Even numbers before:", n)

for i in even_numbers:
    print(i)

