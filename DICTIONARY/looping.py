student = ['ramu,17,15,12,14,False,True,9621852114']

stdDict={
    'name':'bille',
    'maths': 17,
    'english':15,
    'hindi':12,
    'age':14,
    'studies':False,
    'delinquent':True,
    'phone':9621852114
}
# looping dict
print('only keys from dictionary in a for loop')
for item in stdDict:
    print(item, end=' ')

print('\nonly values from dictionary in a for loop')
for item in stdDict:
    print(stdDict[item], end=' ')

print('\nkey and values both from dictionary in a for loop')
for item in stdDict:
    print(item, stdDict[item], end=' ')

print('\nkey and values both from dictionary in a for loop')
for k,v in stdDict.items():
    print(k,'=>',v, end=' ')