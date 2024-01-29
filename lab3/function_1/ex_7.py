def has33(list):
    has = False
    for i in range(len(list)):
        if list[i] == 3 and list[i + 1] == 3:
            has = True
            break
        else:
            continue
    if has:
        print("True")
    else:
        print("False")

list = []
while True:
    x = int(input())
    if x == 0:
        break
    else:
        list.append(x)

has33(list)