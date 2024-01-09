from Groceries import grocery
import matplotlib.pyplot as plot
import numpy as num

def user_menu():
    print("""
User Menu
-------------------
1. Display Grocery Products
2. Print Current Price
3. Plot Price Trend
4. Plot Price Comparison
5. Average/min/max Price
6. Store Comparison
7. Add New Prices
Enter -1 to exit menu
   """)

def current_price(product):
    price = grocery [product][5]
    print(price)
def product_plot(line,product):
    fig=plot.figure()
    arrayY=num.array(grocery[product][::-1])
    arrayX=num.array(range(1,7))
    if line=="scatter":
        plot.scatter(arrayX,arrayY)
    else:
        plot.plot(arrayX,arrayY)
    plot.xlabel("week"), plot.ylabel("price"), plot.title(f"Price of {product} per week")
    plot.show()

def comparison_plot():
    plot.figure('All items')
    for i in grocery:
        array_y=num.array(grocery[i][::-1])
        array_x=num.array(range(1,7))
        plot.xlabel('week'), plot.ylabel('price:'), plot.title(f'Price of all items per week')
        plot.plot(array_x, array_y, label=i)
        plot.legend(framealpha=0.5)
    plot.show()                                                     
                                                         
                                                         
                                                         