#This is our first number gussing game

import random

n = random.randint(1,99)

guess = int(input("Enter an integer from 1 to 99: "))

while 1:
    if guess < n:
        print("Guess is low")
        guess = int(input("Enter an Integer 1 to 99: "))
    elif guess > n:
        print("guess is high")
        guess = int(input("Enter an Integer 1 to 99: "))
    else:
        print("You guessed it!")
        break

