# Exercise 5
# By Monico Luis
# Date 29 Jan 2020
# Description: A program with a game of Jan-Ken-Po

import random
import math

print("Let's play Jan-Ken-Po!\n")
userChoice = int(input("Make your choice! 1 is rock, 2 is paper, 3 is scissors: "))
compChoice = int(random.randint(1,3))

print ("")

if userChoice == 1:
    print ("The user has chosen rock!")
    
elif userChoice == 2:
    print ("The user has chosen paper!")

else:
    print ("The user has chosen scissors!")

print ("")

if compChoice == 1:
    print ("The computer has chosen rock!")

elif compChoice == 2:
    print ("The computer has chosen paper!")

else:
    print ("The computer has chosen scissors!")

print ("")

if userChoice == 1:
    if compChoice == 1:
        print ("It's a tie!")
    elif compChoice == 2:
        print ("The user lost!")
    else:
        print ("The user won!")
            
if userChoice == 2:
    if compChoice == 1:
        print ("The user won!")
    elif compChoice == 2:
        print ("It's a tie!")
    else:
        print ("The user lost!")

if userChoice == 3:
    if compChoice == 1:
        print ("The user lost!")
    elif compChoice == 2:
        print ("The user won!")
    else:
        print ("It's a tie!")
