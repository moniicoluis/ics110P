# Exercise 13
# By Monico Luis
# 03 April 2020
# Purpose: A program to demonstrate the uses of classes

import PlayingCard

cardOne = PlayingCard.PlayingCard()
cardTwo = PlayingCard.PlayingCard()

print("Welcome to a card game! We'll draw a card and you will guess if it is higher or lower than your previous one!\n")


# Purpose: Draws a card for the player.
# Effects: Prints out the first card drawn.
# Input: None
def drawcard():
    cardOne.drawCard()
    cardTwo.drawCard()
    print ("Your first card is the " + cardOne.toString())

# Purpose: Asks the user for their guess, and tells whether or not if it is a win, lose, or tie.
# Effects: Prints out the second card and the results.
# Input: None
def guess():
    guess = input("Would the next card be higher or lower? ")
    if guess == "higher":
        if int(cardOne.getFace()) > int(cardTwo.getFace()):
            print("The card we chose was " + cardTwo.toString() + "! It was lower. You lost.")
        elif int(cardOne.getFace()) < int(cardTwo.getFace()):
            print("The card we chose was " + cardTwo.toString() + "! It was higher. You won!")
        elif int(cardOne.getFace()) == int(cardTwo.getFace()):
            print("The card we chose was " + cardTwo.toString() + "! It is the same value! Its a tie!")
    elif guess == "lower":
        if int(cardOne.getFace()) > int(cardTwo.getFace()):
            print("The card we chose was " + cardTwo.toString() + "! It was lower. You won!")
        elif int(cardOne.getFace()) < int(cardTwo.getFace()):
            print("The card we chose was " + cardTwo.toString() + "! It was higher. You lost.")
        elif int(cardOne.getFace()) == int(cardTwo.getFace()):
            print("The card we chose was " + cardTwo.toString() + "! It is the same value! Its a tie!")

# Purpose: Main function
# Effects: Runs the code, asks the user if they want to continue, and loops it/
# Input: None
def main():
    drawcard()
    guess()
    userInput = input("Would you like to continue? ")
    print("")
    while userInput == "yes":
        main()
        break


if __name__ == '__main__':
    main()
