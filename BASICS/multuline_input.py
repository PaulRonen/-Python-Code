all_data = ''                    # blank string

while True:               # infinite looop by default
    line = input('-')
    if not line:           # if line is not entered
        break              # stop loop
    all_data += line+'\n'        # add the line to all data

print('your data')      #display the data
print(all_data)
print('you entered',len(all_data),'chars')