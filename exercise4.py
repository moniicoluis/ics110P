# Exercise 4
# By Monico Luis
# 27 Jan 2019
# DESCRIPTION: A program that demonstrates Python arithmetic using math library

import math

print ("This is the square root of 7.5: " + str(math.sqrt(7.5)))
print ()
print ("This is the factorial of 7: " + str(math.factorial(7)))
print ()
print ("This is the greatest common divisor of 2028 and 6591: "
       + str(math.gcd(2028, 6591)))
print ()
print ("This is the circumference of a cricle having radius 11: "
       + str(2*math.pi*11))
print ()
print ("This is the area of a circle having radius 11: " + str(math.pi*(11**2)))
print ()
print ("This is the radius of a circle having circumference of 38: "
       + str(38/(math.pi*2)))
print ()
print ("This is the hypotenuse of a right triangle having two other sides of 45 and 62: "
       + str(math.hypot(45, 62)))
print ()
print ("This is side a of a right triangle having side b=12 and hypotenuse=19: "
       + str(math.sqrt(19**2-12**2)))
print ()
print ("This is the radian measurement of 75 degree angle: "
       + str(math.radians(75)))
print ()
print ("This is the sine of a 75 degree angle: "
       + str(math.sin(math.radians(75))))

