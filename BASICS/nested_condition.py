print('you see three doors select 1 from them')
door = input('1 or 2 or 3')

if door == '1':
    print( 'you enter the room, the is dark')
    print( 'you see two glowing eyes')
    print( 'what will u do ?')
    ans = input('run/stand/attack')
    if ans == 'run':
        print('you stuble and get hurt')
    if ans =='attack':
        print('yoy attack to the glowing eues but they are glowing candles')
    if ans=='stand':
         print('nothing happens')

if door == '2':
    print('it was a trap, you die')
if door =='3':
    print(' thir is wall fool')
