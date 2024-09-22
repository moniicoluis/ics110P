# Exercise 6
# By Monico Luis
# 29 Jan 2019
# Description: A program to calculate the area of a shape.

import math

print("Let's calculate the area of a shape!\n")
userShape = input ("Make your choice! Choose between a circle, square, rectangle, and triangle:\n").lower()

if userShape == "circle":
    radius = float (input ("Enter the radius of the circle: "))
    print ("The area of a circle with the radius of " + str(radius) + " is "
           + str(math.pi*radius**2))
elif userShape == "square":
    side = float (input ("Enter the side of the sqaure: "))
    print ("The area of a square with the side of " + str(side) + " is "
           + str(side**2))
elif userShape == "rectangle":
    length = float (input ("Enter the length of the rectangle: "))
    width = float (input ("Enter the width of the rectangle: "))
    print ("The area of a rectangle with the length of " + str(length)
           + " and the width of " + str(width) + " is " + str (length*width))
else:
    base = float (input ("Enter the base of the triange: "))
    height = float (input ("Enter the height of the triangle: "))
    print ("The area of a triangle with the  base of " + str(base) + " and the height of "
           + str(height) + " is " + str(0.5*base*height))
    
