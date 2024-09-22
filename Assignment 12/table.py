# table.py
# By Monico Luis
# 24 March 2020
# Description: A module to be imported into exercise12.py

# Purpose: Creates a table for the products, price, quantity, and the extended value.
# Effects: None, besides output
# Input:
#           productList = A list of the products
#           priceList = A list of the prices
#           quantList =  A list of the quantities

def table(productList, priceList, quantList):
    print ("Products       Price  Quantity  Value")
    for idx in range(len(productList)):
        print (productList[idx],"\t",priceList[idx],"\t",quantList[idx],"\t",(priceList[idx]*quantList[idx]))


# Purpose: Displays the grand total of all the products.
# Effects: None, besides output
# Input:
#           priceList = A list of the prices
#           quantList =  A list of the quantities

def total(priceList, quantList):
    total = list()
    for idx in range(len(priceList)):
        total.append(float(priceList[idx]*quantList[idx]))
    print ("Total: ",sum(total))
        
