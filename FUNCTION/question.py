'''Use the file from gutenburg to read and
count the words and then store the answer in a new file
like this
a  12
to  123
hi  45
this  343
Make this a one or more function program
'''
from string import punctuation

def question1_solver(read_file_path,save_file_path='result.txt'):
    # read the file and store in a variable
    file=open(read_file_path,encoding='utf-8')     #read
    content=file.read()
    file.close()

    # remove every punctuations
    for punc in punctuation:
        content=content.replace(punc,'')
    
    # make every thing lowercase and split in words
    words=content.casefold().split()
    print(f'total words are : {len(words)}')

    # create an empty file
    with open(save_file_path,'w') as file2 :    #create
        # counting the words
        for word in set(words):
            count=words.count(word)
            file2.write(f'{word} : {count}\n')

question1_solver('flick.txt')
