def reverse_string(string):
    x = string.split(' ')
    words = ' '.join(x[::-1])
    print(words)

s = input()
reverse_string(s)