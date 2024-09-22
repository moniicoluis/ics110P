# Exercise 9
# By Monico Luis
# 12 February 2020
# Description: A program where you guess the number

import random
import math

compNum = random.randint(1,100)

print ("A computer will choose a number between 1 and 100. Let's guess it!")

def main():
    i = 0
    while i < 7:
        userGuess = int( input("Enter your guess: "))
        if int(userGuess) > compNum:
            print ("Try a little lower.")
        elif int(userGuess) < compNum:
            print ("Try a little higher.")
        elif int(userGuess) == compNum:
            print ("Good job! The computer chose " + str(compNum))
            break
        i += 1
    

if __name__ == "__main__":
    main()
