def palindrom(string):
    if string == ''.join(reversed(string)):
        print("YES!")
    else:
        print("No")


string = input("Enter your string:")
palindrom(string)