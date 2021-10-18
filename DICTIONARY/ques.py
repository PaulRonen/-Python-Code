'''wap to create a dict contain following sequence
1:1
2:4
3:9
4:16
...
100:10000

hint use loop , dont do it manaully
'''

'''wap to sort dictionary of  5 elemnt .
you can put any thing inside the dictionary

'''

square=dict()
for x in range(1,101):
    square[x]=x**2
print(square) 



x = {
    'r':'red',
    'g':'green',
    'c':'cyan',
    'y':'yellow',
    'bk':'black',
}

print(dict(sorted(x.items())))

