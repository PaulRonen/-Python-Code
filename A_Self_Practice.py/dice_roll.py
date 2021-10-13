import random
while True:
    print(''' 1. roll a dice 
   2. exit''')
    user = int (input('what u wanna do \n'))
    if user ==1:
        nums = random.randint(1,6)
        print(nums)
    
        
        