from random import *

print("Hello! What is your name ?")
name = input()

print(f"Well, {name}, I am thinking of a number between 1 and 20.\nTake guess.")
num = int(input())

x = randint(1, 20)
cnt = 0
temp = True
while temp:

    if num == x:
        cnt += 1
        print(f'Good job, {name}! You guessed my number in {cnt} guesses!')
        temp = False
    elif num < x:
        cnt += 1
        print("Your guess is too low.\nTake a guess.")
        num = int(input())
    elif num > x:
        cnt += 1
        print("Your guess is too high.\nTake a guess.")
        num = int(input())
