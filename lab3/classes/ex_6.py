def is_prime(num):
    cnt = 0
    if num < 2:
        return False
    else:
        for i in range(1, num + 1):
            if num % i == 0:
                cnt += 1
    
    if cnt <= 2:
        return True
    else:
        return False

non_stop = True
num_list = []
while non_stop:
    x = int(input())
    num_list.append(x)
    if x == 0:
        non_stop = False
    

result = filter(lambda num: is_prime(num), num_list)
print(list(result))


