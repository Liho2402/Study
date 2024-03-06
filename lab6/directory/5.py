import os
import json

x = int(input("Number of words in list: "))
list_of_words = []

for i in range(x):
    word = input("Enter words: ")
    list_of_words.append(word)

with open("zapisi.txt", "w") as data:
    for item in list_of_words:
        data.write("%s\n" % item)
    print("Done")
    data.close()

