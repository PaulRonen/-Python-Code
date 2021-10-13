x = [12,15,6,7,3,2]
words = 'pYTHON IS THE BEST LANGUAGE FOR COADING'.split()

'''
map() - modern way for mapping a sequence for a operatin in 1 line
filter() - modern way for filtering a sequence using condition i  1 line

'''
'''
map() and reduce() use lazy object concept, in which data is not 
consuming memeory until its is casted a particular datatyprs like 
list , tuple , set
'''
x2 = list(map(lambda i : i ** 2,x))
y = [2,5,3,2,6,2,]

xy = list(map(lambda i,j : i+j,x,y))
print(xy)

f = lambda i,j: i+j
if len(x)== len(y):
    xy = list(map(f,y,y))
print(xy)


#filter

words_with_a = list(filter(lambda i : 'n'in i ,words))
print(words_with_a)