def reverse(n):
    for i in range(n, 0, -1):
        yield i


n = int(input())
obratka = reverse(n)

print("Reverse number")

for i in obratka:
    print(i)
