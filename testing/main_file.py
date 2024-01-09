#!/usr/bin/env python
# coding: utf-8

# In[5]:


from calc_grocery import change_price, minmax, price_comparison
from display_grocery import user_menu, product_plot, comparison_plot, current_price
from Groceries import grocery

user_menu()
funcs= []

while len(funcs)<7:
    user_input= int(input("Enter a value between 1-7: "))
    if user_input not in funcs:
        funcs.append(user_input)
        print(funcs)
        
    if user_input in (2,3,5,6,7):
        product=input('Enter the product name: ')
        
        if user_input==2:
            current_price(product)
        elif user_input == 3:
            line_type= input('Enter if you want a "scatter line" or "line": ')
            product_plot(line_type,product)
        elif user_input==5:
            values=minmax(product)
            print(values)
        elif user_input==6:
            store_name= input('Enter the store name: ')
            price= float(input("Enter the price to compare with: "))
            price_comparison(store_name,price,product)
        elif user_input==7:
            new_price=int(input('Enter the price to add: '))
            change_price(product,new_price)
    elif user_input==1:
        print(grocery.keys())
        
    elif user_input==4:
        comparison_plot()
    
    elif user_input== -1:
        break
        
            
        


# In[ ]:





# In[ ]:




