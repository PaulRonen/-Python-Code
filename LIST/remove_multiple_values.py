x = [1,1,2,2,3,3,3,3,2
,2,2,3,3,32,2,3,3,1,2,3,
2,2,3,3,3,3,3,3,2,2,2,2
,1,1,2,2]

# remove all the 3s in the list
print(x)

y=x.copy()

for i in range (x.count(3)):
    x.remove(3)

print('3s are removed')
print(x)

# remoing all 3s with pop and index

while 3 in y :
    idx = y.index(3)
    y.pop(idx)
print(y)