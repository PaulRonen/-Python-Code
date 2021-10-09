# Q23 ask user to enter a string and check if the string contains fyi

str = input("Enter a sentence : ")
idx=str.find("fyi")
if idx==-1:
    print("The sentence does not contains 'fyi'")
else:
    print("The sentence contains 'fyi'")