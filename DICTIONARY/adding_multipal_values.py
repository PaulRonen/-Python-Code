menu = {
    'veg machurian' :189.00,
    'fried rice': 100.00,
    'momos' : 80.00
}

new_memu = {
    'chicken machurian' :259.00,
    'chicken momos': 160.00
}

print('before update',menu)
menu.update(new_memu)

print('after update',menu)

update_menu = {
    'veg momos' :100.00,
    'veg chowmein': 120.00
}
print('update menu',update_menu)
menu.update(update_menu)
