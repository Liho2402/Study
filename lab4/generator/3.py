def gen_iter(n):
    for i in range(n):
        if i % 12 == 0:
            yield i


n = int(input())
numbers = gen_iter(n)
print("That divisible on 3 and 4:")
for i in gen_iter(n):
    print(i)


