'''wap to ask the user his/her expenses on didd items .takes around 15 keys and 
value from user & then perform sum& average on the value
'''

items = {}

print("Enter Item & Expenses-->")
for i in range (15):

    k = input('enter a item-->')
    v = int(input('enter a price-->'))
    items[k] = v

total = sum (list(items.values()))
avg = sum(list(items.values()))/len(items)
print(f'Total is{total},Avg is{avg}')