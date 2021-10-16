a =(1,2,3)
b =(12,34,56)

print(a,b)
print(type(a),type(b))

c = ('Kakarot','Prince Vegeta','Majin Buu')
print(c[0])# accessing value from index
print(c[1])
print(c[-1])

#creating tuple from existing data
name = 'Rahul'
nameT =tuple(name)
print(nameT) # new varible contains tuples , create

values = [1299,239,8546,8416]
values = tuple(values) # original variable converted to tuple < update
print(values)

a = 12
b = 45

x = a,b
print(x)