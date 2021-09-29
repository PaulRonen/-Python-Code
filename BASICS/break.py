# break keyword is imp in loop as it allows us to sstop the loop before completion

name = input('what is your name:')
size = len(name)
while size > 0:
     size -= 1
     if name[size] == ' ':
         print('\nspace found in name')
         break
     else:
         print(name[size], end='')