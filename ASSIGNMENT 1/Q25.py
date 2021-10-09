# Q25 calculate the average word length of the following paragraph.
#this is a paragraph which is written just for the purpose of providing content to let the average word length be calculated


para = "this is a paragraph which is written just for the purpose providing content to let the average word length be calculated"

words = para.split(" ")
sum_of_words=0
for ch in words:
    num=len(ch)
    sum_of_words+=num
avg = sum_of_words/len(words)
print(avg)