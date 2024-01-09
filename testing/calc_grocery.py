from Groceries import grocery
import numpy as num

def minmax(product):
    array= num.array(grocery[product])
    average=num.mean(array)
    maximum=num.max(array)
    minimum=num.min(array)
    data=[average, maximum, minimum]
    return data
def price_comparison(store_name,price_s,product):
    price= grocery[product][5]
    
    if price_s>=price:
        print("Come to our store to save money")
    else:
        print("we will match that price")
def change_price(product, new_price):
              price= grocery[product]
              price.pop(5), price.insert(0,new_price)
              print(price)