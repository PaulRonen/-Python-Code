msg =''' Dragon Ball Z continues the adventures of Son Goku 
in his adult life as he and his companions defend the Earth against villains including aliens (Vegeta, Frieza)
androids (Cell), and magical creatures (Majin Buu). At the same time, the story parallels the life of his son
, Gohan, as well as the development of his rivals, Piccolo and Vegeta.'''

words = msg.split()
print(words)

for item in words :
    print(f'{item}->{words.count(item)}')