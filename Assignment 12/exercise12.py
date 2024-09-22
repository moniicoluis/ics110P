# Project 12
# By Monico Luis
# 12 March 2020
# Description: A program demonstrating lists and file I/O

productList = list()
productFile = open("products.txt.","r")
for line in priceList:
    priceList.append(line[:-1])


    
def price():
    priceList = list()
    priceFile = open("prices.txt","r")
    for line in priceFile:
        priceList.append(float(line))
    return priceList

def quantities():
    quantList = list()
    quantFile = open("quantities.txt", "r")
    for line in quantFile:
        quantList.append(int(line))
    return quantList


print (productList)

