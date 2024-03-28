def spy_game(list):
    if len(list) == 0:
        return "No game"
    else:
        string = ''
        for i in list:
            if i == 0 or i == 7:
                string += str(i)
            else:
                continue
    
    if string == '007':
        print("True")
    else:
        print("False")

print("Pleasse write a number of numbers in list")
n = int(input())
list = []
for i in range(n):
    list.append(int(input()))

spy_game(list)