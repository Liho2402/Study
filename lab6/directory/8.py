import os
import json

def delete_path(file_path):
    if not os.path.exists(file_path):
        print("Write correct path")
        return 0
    else:
        if not os.access(file_path, os.W_OK):
            print("File can not be changed")
        else:
            os.remove(file_path)
            print(f"{file_path} was delete")

file = input("Please print path, which we need to delete: ")
delete_path(file)

