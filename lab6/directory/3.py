import os

def exists_file(filename):
    return os.path.exists(filename)

path = input("Enter the path of the: ")

if exists_file(path):
    print("This path exists:", os.listdir(path))
else:
    print("file does not exist")