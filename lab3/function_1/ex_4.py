def filter_prime(list):
    for i in list:
        if i > 0 and i != 0 and i != 1:
            cnt_in_list = 0
            k = 1

            while k != i + 1:
                if i % k == 0:
                    cnt_in_list += 1
                k += 1

            if cnt_in_list <= 2:
                print(i , end=' ')
        else:
            continue

x = int(input())
list = []
for i in range(x):
    list.append(int(input()))
filter_prime(list)