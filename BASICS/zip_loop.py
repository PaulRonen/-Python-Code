
num =[12,34,61,85,]
num2=[45,84,78,21]
num3=[1,2,4,5,8,8,6,2,5,9,2]

for i,j in zip (num,num2):
    print(i,j)

for i,j in zip (num,num2):
    print(i+j)

for i,j,k in zip (num,num2,num3):
    print(i,j,k)