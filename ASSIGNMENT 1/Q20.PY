# Q20 Ask user to input string, print found if any of the character is upper case.

str = input("Enter a string : ")
flag=0
for character in str:
    if character.isupper()==True:
        flag=1
if flag==1:
    print("GOATCHA")