x = [1,1,2,2,3,3,3,3,2,2,2,3,3,32,2,3,3,1,2,2,2,3,3,3,3,3,3,2,2,2,2,1,1,2,2]
print(x)

print('occerence of 1=',x.count(1))
print('occerence of 2=',x.count(2))
print('occerence of 3=',x.count(3))
print('occerence of 5=',x.count(5))
print('occerence of 10=',x.count(10))

a =['chicago','new york','dallas']
b =[12,45,13]
c =['nevada',57,'massouri',58]
print(a)
a.sort()
print(a)

print(b)
b.sort(reverse=True)
print(b)
#error
#print(c)
#c.sort()
#print(c)

y = [1,1,1,2,2,33,25,5,12,32,23,2,5]
print(y)
y.reverse()
print(y)
idx = y.index(1223)
print('1223 found at',idx)
idx= y.index(2)
print('2 found at',idx)

if 123 in y:
    idx = y.index(123)
    print('123 found at',idx)

z =x.copy()
print(z)
print(x)
x.sort()
print(x)
print(z)