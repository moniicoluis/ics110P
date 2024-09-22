# Exercise 8
# By Monico Luis
# Date 30 Jan 2020
# Description: A program that asks the user if they want to calculate the perimeter or area and displays it.

import math

print ("Let's calculate the area or perimeter of various basic shapes!")

print ("")

userInput = input (" Make your choice! Choose between area/perimeter: ")

print ("")

if userInput == "area":
    print("Let's calculate the area of a shape!\n")
    userShape = input ("Make your choice! Choose between a circle, square, rectangle, and triangle: ").lower()

    print ("")

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

else:
    print ("Let's calculate the perimeter of a shape!\n")
    userShape = input ("Make your choice! Choose between circle/square/rectangle/triangle: ")

    print ("")

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


    
