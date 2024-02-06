def gen_number(x):
    for i in range(1, x + 1):
        yield i ** 2


n = int(input())
gen_generated = gen_number(n)

print(f"Square numbers before {n}")
for j in gen_generated:
    print(j)