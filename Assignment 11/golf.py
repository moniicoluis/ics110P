# golf.py
# by Monico Luis
# 26 February 2020
# Description: Module to be inputted into exercise11.py

# Purpose: Lists the hole, par, and strokes of a golf player.
# Effects: None, besides output
# Input:
#           par: the pars of a hole in the game of golf
#           strokes: the player's strokes of hole in a game of golf
def main(par, strokes):
    print('Hole    Par   Strokes')
    for val in range(len(par)):
        print((val+1),'\t',par[val],'\t',strokes[val])


# Purpose: Count the number of birdies that a player has made.
# Effects: None, besides output
# Input:
#           par: the pars of a hole in a game of golf
#           strokes: the player's strokes of a hole in a game of golf
def birdies(par, strokes):
    birdies = 0
    for val in range(len(par)):
        if int(par[val] - 1) == int(strokes[val]):
            birdies = int(birdies + 1)
    return birdies

# Purpose: Count the number of eagles that a player has made.
# Effects: None, besides output
# Input:
#           par: the pars of a hole in a game of golf
#           strokes: the player's strokes of a hole in a game of golf
def eagles(par, strokes):
    eagles = 0
    for val in range(len(par)):
        if int(par[val] - 2) == int(strokes[val]):
            eagles = int (eagles + 1)
    return eagles

# Purpose: Count the number of bogies that a player has made.
# Effects: None, besides output
# Input:
#           par: the pars of a hole in a game of golf
#           strokes: the player's strokes of a hole in a game of golf
def bogey(par, strokes):
    bogey = 0
    for val in range(len(par)):
        if int(par[val] + 1) == int(strokes[val]):
            bogey = int(bogey + 1)
    return bogey

# Purpose: Count the number of double bogies that a player has made.
# Effects: None, besides output
# Input:
#           par: the pars of a hole in a game of golf
#           strokes: the player's strokes of a hole in a game of golf
def doublebogey(par, strokes):
    doublebogey = 0
    for val in range(len(par)):
        if int(par[val] + 2) == int(strokes[val]):
            doublebogey = int(doublebogey + 1)
    return doublebogey
            
# Purpose: List the holes that the player has made par
# Effects: None, besides output
# Input:
#           par: the pars of a hole in the game of golf
#           strokes: the player's strokes of hole in a game of golf 
def madepar(par, strokes):
    for val in range(len(par)):
        if int(par[val]) >= int(strokes[val]):
            print ("Player has made par on hole ", int(val+1))
    print ("")

# Purpose: List the holes that the player has missed par
# Effects: None, besides output
# Input:
#           par: the pars of a hole in the game of golf
#           strokes: the player's strokes of hole in a game of golf 
def missedpar(par, strokes):
    for val in range(len(par)):
        if int(par[val]) < int(strokes[val]):
            print ("Player has missed par on hole ", int(val+1))
    print ("")

# Purpose: A frequency table of the number of strokes
# Effects: None, besides output
# Input:
#           strokes: the player's strokes of hole in a game of golf
def freqtable (strokes):
    print ("Hole     Number")
    for val in range (8):
        print((val+1),'\t',(strokes.count(val+1)))
