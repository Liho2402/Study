from time import sleep
from math import sqrt
num = int(input("Input your number: "))
mill = int(input("Enter milliseconds: "))

sleep(mill / 1000)

print(f"Square root of {num} after {mill} miliseconds is {sqrt(num)}")