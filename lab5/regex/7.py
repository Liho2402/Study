
txt = input("Enter word in snake case type: ")

x = ''.join(word.title() for word in txt.split('_'))

print(x)


