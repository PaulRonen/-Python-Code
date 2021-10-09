# Q16 Ask user to input a string and check if the string ends with '?

msg = input("Enter a string : ")
if msg[-1]=="?":
    print("Sentence ends with '?'")
else:
    print("Sentence doesn't ends with '?'")