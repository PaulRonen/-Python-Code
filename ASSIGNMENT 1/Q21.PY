# Q21 Extract names from the following string and store them in a list.
#names = 'Joe, David, Mark, Tom, Chris, Robert'

names = 'Joe, David, Mark, Tom, Chris, Robert'
words=names.split(", ")

x=[]
for i in words:
    x.append(i)
print(x)