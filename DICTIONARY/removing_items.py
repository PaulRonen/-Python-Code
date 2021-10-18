hotel_menu ={
    'veg machurian' :189.00,
    'fried rice': 100.00,
    'momos' : 80.00,
    'chicken machurian' :259.00,
    'veg momos' :100.00,
    'veg chowmein': 120.00,
    'costly food item 1': 999
    
}

#remove
if'costly food item 1 ' in hotel_menu:
 rmv_value = hotel_menu.pop('costly food item 1')
 print(rmv_value)
 print(hotel_menu)

rand_value = hotel_menu.popitem()
print(rand_value)
print(hotel_menu)

hotel_menu.clear()
print(hotel_menu)