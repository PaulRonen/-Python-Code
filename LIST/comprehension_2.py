'''
-comprehension =when we want to create a lst from an existing list i n 1 line
-mapping = generate same size sequence from existing sequence
-filtering = select or create a smaller sequnce from existing one, using condition

'''
'''
syntax
newlist = [opreation loop-for-existinglist !conditiom!]
'''
x=[2,3,51,52,456,4,54,4,1,2,3,6,5,4,8,9]
#mapping

x2 = [i**2 for i in x]

print(x)
print(x2)

#filter
x_odd = [i for i in x if i%2!=0]
print(x_odd)
