# we have continue keyword
# WHICH IS USED TO SKIP A lop step
# it can be used in for and while both

i = int(input('enter value of i: '))

while i > 0:
    if i % 3 == 0:
        i-=1
        continue
    print(i)
    i-=1




# we can skip continue keyword
while i > 0:
    if i%3!=0:
        print(i)
    i-=1