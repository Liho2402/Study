import os
import json

def paste(first_file_name, second_file_name):
    first_file = open(f"{first_file_name}.txt", "r")
    data = first_file.read()

    second_file = open(f'{second_file_name}.txt', "a")
    info = second_file.write(data)

    print(f"File {first_file_name} was copy in {second_file_name}")
    first_file.close()
    second_file.close()


name = input("Print name first file: ")
name_sec = input("Print name second file: ")

paste(name, name_sec)