words = {} #emt dict

words['alpha'] = "number one,the starting value, or the top value"
print("User input-->")
for i in range (3):

    k = input('enter a word-->')
    v = input('enter a meaning-->')
    words[k] = v

#full
print(words)

#rading a particular value
print(words['alpha'])
print(words.get('alpha','not found'))

print(words.__getattribute__b
('beta'))
print(words.get('beta','not found'))
