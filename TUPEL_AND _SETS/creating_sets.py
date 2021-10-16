x = set () #empty set

x = {1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1,}
print(x)

words = {'harry','ron','hegrid','bucky','dumbaldoor','hermaine'}
print(words)

for value in words :
    print(value,end=' ')

quote = '“Many of life’s failures are people who did not realize how close they were to success when they gave up.”'
quote_char = set (quote.lower())
print(quote_char)
