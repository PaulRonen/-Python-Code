from string import ascii_lowercase

content = '''
Dragon Ball Z continues the adventures of Son Goku in his adult life as he and his companions defend the Earth
against villains including aliens (Vegeta, Frieza), androids (Cell), and magical creatures (Majin Buu).
 At the same time, the story parallels the life of his son, Gohan, as well as the development of his rivals,
  Piccolo and Vegeta. 
'''

num_of_a =content.count('a')
print(f'a occurs {num_of_a} times')

in_counter = content.count('in')
print(f'`in` occurs {in_counter} times')

# counting all alphabets

max_freq = 0
most_freq_letter = ''
for letter in ascii_lowercase:
    counter = content.casefold().count(letter)
    print(f'{letter} found {counter} times')
    if max_freq < counter:
        max_freq = counter
        most_freq_letter = letter

print(f"the {most_freq_letter} has highest frequency: {max_freq}")