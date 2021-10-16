mytuple = 12,12351,65,15,11,81,5,41,1,2,33,2,5,54,52,18,41,52,541,651,541,62,3521

print(mytuple.count(1),'occurance of 1')
print(mytuple.count(65),'index has 65')

for i in mytuple:
    print(i,end = ' ')
print('\nreversed')

for i in  mytuple[::-1]:
    print(i,end=' ')