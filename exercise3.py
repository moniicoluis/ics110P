# Exercise 03
# By Monico Luis
# Date, January 22, 2020
# DESCRIPTION: A program to convert from miles to kilometers and vice versa.

import argparse

dist_miles=0
dist_kilometers=0

KILOMETERS_IN_MILE = 1.60934

parser = argparse.ArgumentParser(description='Trying out user input')

parser.add_argument('dist_miles', type=float,  
                    help='distance in miles')
parser.add_argument('dist_kilometers', type=float,  
                    help='distance in kilometers')

args = parser.parse_args()

dist_miles = args.dist_miles
kilometers = args.dist_miles*KILOMETERS_IN_MILE

dist_kilometers = args.dist_kilometers
miles = args.dist_kilometers/KILOMETERS_IN_MILE

print(kilometers)

print()
print()
print()

print(miles)
