'''
-comprehension =when we want to create a lst from an existing list
-mapping = generate same size sequence from existing sequence
-filtering = select or create a smaller sequnce from existing one, using condition

'''

#mapping without comprehension

#squares
x =[1,2,3,4,5,6,7,8,9,10]

x2=[]
for i in x :
    sqr = i** 2
    x2.append(sqr)

print(x)
print(x2)

# cubes
x3=[]
for i in x :
    cube = i** 3
    x3.append(cube)


print(x3)


#filtering without comprehension

# even nos.

x_even = []
for i in x:
    if i%2 ==0:
        x_even.append(i)

print(x)
print(x_even)

#