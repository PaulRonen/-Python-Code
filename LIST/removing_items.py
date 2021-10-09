# REMOVE
# searching value

colors =[ 'yellow','green','blue','pink','black','pink']
colors.remove('yellow')
print(colors)
if 'jellow' in colors:
    colors.remove('jellow')
print(colors)
if 'pink' in colors:
    colors.remove('pink')
print(colors)


#pop
#remove value by idx - if not given remove last
#the removed value can be stored in a variable
colors.pop(1)
print(colors)
seprated_value =colors.pop(2)
print(colors)
print(seprated_value)

colors.pop()
print