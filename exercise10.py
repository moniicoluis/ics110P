# Exercise 10
# By Monico Luis
# 13 February 2020
# DESCRIPTION: A program that sings a song with user input.

userNum = int(input("Enter the number of bottles of milk on the wall: "))
print ("")

import math

def bottles(bot):
   if int (bot) == 1:
      print("1 bottle of milk on the wall.")
      print("1 bottle of milk!")
      print("Take one down, pass it around.")
      print("No more bottles of milk on the wall!")
      return('')
   elif int (bot) != 1:
      print(bot, " bottles of milk on the wall.")
      print(bot, " bottles of milk!")
      print("Take one down, pass it around.")
      if int (bot) == 2:
         print("1 bottle of milk on the wall!")
         return('')
      else:
         print((bot - 1), " bottles of milk on the wall!")
         return('')

def main():
   bot = userNum
   while int (bot) > 0:
      print (bottles(bot))
      bot -= 1


if __name__ == "__main__":
   main()
