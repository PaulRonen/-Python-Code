words = {'harry','ron','hegrid','bucky','dumbaldoor','hermaine'}
print(words)

if 'harry' in words :
    words.remove('harry')
print(words)

remvd_value = words.pop()
print(words)
print(remvd_value)

words.clear()
print(words)