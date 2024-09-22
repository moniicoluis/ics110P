# Assignment 12
# By Monico Luis
# 22 March 2020
# Description: A program to demonstrate I/O and the use of lists by displaying the products, price, and quantities of items. 

import table

productList = list()
productFile = open("products.txt","r")
for line in productFile:
    productList.append(line[:-1])

priceList = list()
priceFile = open("prices.txt","r")
for line in priceFile:
    priceList.append(float(line))

quantList = list()
quantFile = open("quantities.txt","r")
for line in quantFile:
    quantList.append(int(line))


table.table(productList, priceList, quantList)

print()

table.total(priceList, quantList)
    
