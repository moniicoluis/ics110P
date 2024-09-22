# Project 11
# By Monico Luis
# Date 24 February 2020
# Description: A program to calculate golf scores 

import golf

par = (5,4,3,4,5,3,4,4,4,4,4,5,3,4,4,3,5,4)
strokes = (4,4,3,5,4,4,6,5,4,4,5,6,3,5,4,4,7,5)


golf.main(par, strokes)

print("")

print ("Player has made " ,golf.birdies(par, strokes), " birdies")

print ("Player has made " ,golf.eagles(par, strokes), " eagles.")
    
print ("Player has made " ,golf.bogey(par, strokes), " bogies.")

print ("Player has made " ,golf.doublebogey(par, strokes), " double bogies.")

print ("")

golf.madepar(par, strokes)

golf.missedpar(par, strokes)

golf.freqtable(strokes)



