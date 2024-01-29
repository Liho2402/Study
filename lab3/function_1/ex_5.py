def permutations(string, current=""):

    if not string:
            print(current)
    else:
        for i in range(len(string)):
            remaining_chars = string[:i] + string[i + 1:]
            permutations(remaining_chars, current + string[i])

string = input()
permutations(string, current=' ')
