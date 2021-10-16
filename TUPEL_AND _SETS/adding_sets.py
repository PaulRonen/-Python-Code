a = {1,2,3}

a.add(129)
a.add('Charbagh')
a.add((1,2,3))
print(a)

# error -> u cannot add a list , dict or set in set
#a.add([1,2,3])
#print(a)

x = [1,2,3,2,1,1,521,3,1,3,1]
a.update(x)
print(a)