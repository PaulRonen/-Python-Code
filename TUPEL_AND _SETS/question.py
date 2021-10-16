# wap to add value from user in a set
# the can add any number of values in the set
# use while loop to perform this task 
# time 10min

x = set ()

while True :
    x = input('ENTER VALUE')
    if not x:
        break
    x.add(x)

print(x)