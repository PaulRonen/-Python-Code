from typing import DefaultDict


marks = {
    'rohan':2,
    'reham':3,
    'sohan':3,
    'mohan':5,
    'gohan':4,
}
name=list(marks.keys())
print(name)

number=list(marks.values())
print(number)

items=list(marks.items())
print(items)

a = 'Ramu'
b = 'shayamu'
c = 'laita'
d = 'bulma'
e = 'rohit'

default_marks = 'N/A'

new_student ={}

new_student = dict.fromkeys([a,b,c,d,e], default_marks)
print(new_student)

position = list(range(1,11))
position_dict = dict.fromkeys(position,'available')
print(position_dict)

copy_of_dict = position_dict.copy()
print(copy_of_dict)