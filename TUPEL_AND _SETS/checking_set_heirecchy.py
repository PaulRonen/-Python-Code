x ={1,5,8,5,2,1,5,6,8,5,2,0,5,}
y ={5,2,0,2,5,5}
z ={5,2,2,2,5,2,2,2,5,2}
a ={4,1,2,5,84,99,54}

print('x is superset of y',x.issuperset(y))
print('x is superset of z',x.issuperset(z))
print('x is superset of a',x.issuperset(a))

print('y is subset of x',y.issubset(x))
print('y is subset of x',y.issubset(z))
print('y is subset of x',y.issubset(a))

print('y is unrelated of x',y.isdisjoint(x))
print('y is unrelated of y',y.isdisjoint(z))
print('y is unrelated of z',y.isdisjoint(a))