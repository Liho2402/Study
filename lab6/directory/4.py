import json

with open("blablab.txt", "r") as info:
    data = len(info.readlines())

    print(f"Lines in txt file: {data}")
