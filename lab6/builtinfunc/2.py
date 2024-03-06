def upper_counter(string):
    cnt = 0
    for letter in string:
        if letter.isupper():
            cnt += 1
    print(f"{cnt} amount of upper letters")

string = input("Your String:")
upper_counter(string)
