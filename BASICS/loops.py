"""
for temp_var in iterable:
    satatement 1
    satatement 2
    ...
    satatement n

iterable can be of
-string
-list
-tuple
-set
-dict
-special function linke range(),zip(),emuerate()
-anything with multipal element
"""

num=[1,2,3,4,5,6,7,11,19]
for i in num:
    print(i)

msg = "we are now using loops"
print('characters in msg:',len(msg))

#traversal
for char in msg :
    if char !='':
        print(char)

#numaric code
for i in range(10):
    print(i, end=",")

