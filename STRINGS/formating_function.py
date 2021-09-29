'''
trivia
2 types of function
-function that will give output
function that will change the original variable
-
'''
name = "we are going to have fun"

uname=name.upper()    #upper case
print(uname)

lname=name.lower()  #lowercase
print(uname)

n1 = name.capitalize()  #
print(n1)

n2 = name.title()#
print(n2)

n3 = name.swapcase()#
print(n3)


n4 = name.casefold() #same as lower  case
print(n4)

word = input('what is your fav DBZ charectar')
spacing = int(input('select number for space'))
print(f'printing{word} with spacing{spacing}')

lword = word.ljust(spacing)
print(lword)
rword = word.rjust(spacing)
print(rword)
cword = word.center (spacing)
print(cword)

char = input('enter a charrectar')
lword= word.ljust(spacing,char)
print(lword)
rword= word.rjust(spacing,char)
print(rword)
cword= word.center(spacing,char)
print(cword)

