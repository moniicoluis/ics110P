# Exercise 7
# By Monico Luis
# Date 30 Jan 2020
# Description: A program to calculate the perimeter of basic shapes

import math

print ("Let's calculate the perimeter of a shape!\n")
userShape = input ("Make your choice! Choose between circle/square/rectangle/triangle: ")

if userShape == "circle":
    radius = float (input ("Enter the radius of the circle: "))
    print ("The perimeter of the cirlce with the radius of " + str(radius) + " is "
           + str(2*math.pi*radius))
elif userShape == "square":
    side = float ( input ("Enter the side of the square: "))
    print ("The perimeter of the square with the side of " + str (side) + " is "
           + str(4*side))
elif userShape == "rectangle":
    length = float ( input ("Enter the length of the rectangle: "))
    width = float ( input ("Enter the width of the rectangle: "))
    print ("The perimeter of the square with the length of " + str(length)
           + " and a width of " + str(width) + " is " + str(2*length + 2*width))
else:
    side1 = float ( input ("Enter the first side of the triangle: "))
    side2 = float ( input ("Enter the second side of the triangle: "))
    side3 = float ( input ("Enter the third side of the triangle: "))
    print ("The perimeter of the triangle with sides of " + str(side1) + ", "
           + str(side2) + ", and " + str(side3) + " is " + str(side1 + side2 + side3))
