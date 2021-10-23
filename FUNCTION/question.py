'''Use the file from gutenberg to read and 
count the words and then store the answer in a new file
like this
a   12
to  123
hi  45
this 343
Make this a one or more function program
'''



file = open('flick.txt')
print(file.read())
file.close()

num_of_a =count('a')
print(f'a occurs {num_of_a} times')

in_counter =count('in')
print(f'`in` occurs {in_counter} times')