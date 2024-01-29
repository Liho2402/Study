def unique(input_list):
    new_list = []
    n = len(input_list)
    
    for i in range(n):
        is_unique = True
        for j in range(i + 1, n):
            if input_list[i] == input_list[j]:
                is_unique = False
                break
        if is_unique:
            new_list.append(input_list[i])

    print(new_list)


list = []
while True:
    x = int(input())
    if x == 0:
        break
    else:
        list.append(x)
unique(list)