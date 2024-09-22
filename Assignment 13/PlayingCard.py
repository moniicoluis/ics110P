# CardGame Application
# By: Monico Luis
# 03 April 2020

import random

class PlayingCard:

    def __init__(self, face = "none", suit = "none"):
        if face == "none":
            self.drawCard()
        else:
            self.face = face

    def drawCard(self):
        self.face = random.randint(2,14)
        self.suit = random.randint(1,4)

    def getFace(self):
        return self.face

    def getSuit(self):
        return self.suit

    def setFace(self, newFace):
        self.face = newFace

    def setSuit(self, newSuit):
        self.suit = newSuit

    def toString(self):
        cardName = ""
        if self.face == 2:
            cardName = "Two of "
        elif self.face == 3:
            cardName = "Three of "
        elif self.face == 4:
            cardName = "Four of "
        elif self.face == 5:
            cardName = "Five of "
        elif self.face == 6:
            cardName = "Six of "
        elif self.face == 7:
            cardName = "Seven of "
        elif self.face == 8:
            cardName = "Eight of "
        elif self.face == 9:
            cardName = "Nine of "
        elif self.face == 10:
            cardName = "Ten of "
        elif self.face == 11:
            cardName = "Jack of "
        elif self.face == 12:
            cardName = "Queen of "
        elif self.face == 13:
            cardName = "King of "
        else:
            cardName = "Ace of "

        if self.suit == 1:
            cardName = cardName + "Spades"
        elif self.suit == 2:
            cardName = cardName + "Clubs"
        elif self.suit == 3:
            cardName = cardName + "Hearts"
        else:
            cardName = cardName + "Diamonds"

        return cardName

