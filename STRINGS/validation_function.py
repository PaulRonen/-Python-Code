value = input('enter something :')

ans=value.isupper()
print('Is this value entered is upper?', ans)

ans=value.islower()
print('Is this value entered is lower?', ans)

ans=value.isalpha()
print('does the value contain alpahbet?', ans)

ans=value.isnumeric()
print('Is this value conatain only number?', ans)

ans=value.isspace()
print('Is tha value contain space?', ans)

ans=value.isprintable()
print('Is this value printable on screen?', ans)

ans=value.isdigit()
print('Is this value contain only digit?', ans)

ans=value.isdecimal()
print('Is this value contain decimal?', ans)

name = "Dr Ram Verma"
if name.startswith("Dr"):
    print('heyy doc')
if name.startswith("mr"):
    print('heyy mister')

file = input('enter the filename:')
if file.endswith('.exe'):
    print(f"{file} is Application file")
elif file.endswith('.doc'):
    print(f"{file} is Word file")
elif file.endswith('.pdf'):
    print(f"{file} is PDF file")
elif file.endswith('.png'):
    print(f"{file} is Image file")
