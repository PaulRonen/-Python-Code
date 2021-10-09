# Q15 Ask user to input a sentence and print each word on a different line.

msg = input("Enter a sentence : ")
words = msg.split(" ")
for i in words:
    print(i)