num = list(range(20))

print(num)

print('first value',num[0])
print('second value',num[1]) 
print('last value',num[-1])

num[0] = 50
num[-1] = 20
num[2] = 20
#update
print(num)

print('first 3 times',num[:3])
print('last 5 items',num[-5]) 
print('all items expert first 2 and last 2 ',num[2 :-2])

print('reverse a list',num[::-1])
print('all even index of list',num[::2])
print('all odd index of list',num[1::2])


