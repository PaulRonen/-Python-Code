num = list(range(5,15))

for element in num:
    print(element)

words = ['This','That','Wish','What']
for item in words :
    print(f'{item}is{len(item)}char')

coords = [[1,2],[3,2],[1,2]]
for i  in coords:
    print(i)

for i in coords :
    print(i[0],i[1])

for idx, value in enumerate(words):
    print(f'{idx}has{value}')

for i in num:
    if i % 3 ==0:
        print(i)