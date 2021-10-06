msg = '''Dragon Ball Z continues the adventures of Son Goku 
in his adult life as he and his companions defend the Earth against villains including aliens (Vegeta, Frieza)
androids (Cell), and magical creatures (Majin Buu). At the same time, the story parallels the life of his son
, Gohan, as well as the development of his rivals, Piccolo and Vegeta.'''

word = msg.split()
print(word)

msg2 =''' Dragon Ball Z continues the adventures of Son Goku 
in his adult life as he and his companions defend the Earth against villains including aliens (Vegeta, Frieza)
androids (Cell), and magical creatures (Majin Buu). At the same time, the story parallels the life of his son
, Gohan, as well as the development of his rivals, Piccolo and Vegeta.'''
sentence = msg2.split(',')

sentence = msg2.split('.')
print(sentence)

gibberish = msg2.split('a')
print(gibberish)

print(f'we found {len(word)})words in msg'
print(f'we found {len(msg2.split() )} word in msg2')

msg3 = 'welcome to jhumritalieaya, you will have fun, just dont steal from us, or you will have no fun'

print('n ->', msg3.split(','))
print('n 2 split ->', msg3.split(',', maxsplit=2))
print('r ->', msg3.rsplit(','))
print('r 2 split ->', msg3.rsplit(',', maxsplit=2))

print(msg3[:18])
