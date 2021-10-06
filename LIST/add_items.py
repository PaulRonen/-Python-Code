x = [] #emptyn list
print('3 number daaal:')
for i in range(3):
    val=input('->')
    x.append(val)

x.append('10')
x.append('Helium')
x.append('True')
#x.append(1,2,3,) error
x.append(['a','b','c'])# append list to the end of the list
print(x)

x.insert(0,200)
x.insert(4,'modiji')
x.insert(-3,'amitshah')
x.insert(2,[1,2,3,4])
print(x)

a = [1,2,3,4]
b = [3,2,3,]

print(a)
print(b)
a.extend(b)
print(a)
b.extend(a)
print(b)


