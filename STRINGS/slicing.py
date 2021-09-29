name = 'vijay deenanath chauhan'

print("size",len(name))

print(name[2],name[3],name[4])  #noob implementation



print(name[2:5])

print(name[6:-8])




# we can skip zerofirst if we want to start from beginning
# we can skip value after colon if we want to stop at end


print(name[:5])   #first five char from0 to 4

print(name[-7:])   # last 7 chars from -7 to end


# syntax for slicing: 
# var[startidx : endidx : gap]


print(name[::2])  # start to end with gap of 2 indexes


# reverse string
print(name[::-1])

print(name[:])  # full name print

print(name[:][::-1][:5])