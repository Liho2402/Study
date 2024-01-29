def palindrom(string):
    if string == string[::-1]:
        print("YES")
    else:
        print("NO")


string = input()
palindrom(string)
