'''
file handling basics
1. read a file- open()
2. write a file- open()
3. update a file- open()
open() function has a option to set mode of file it return a file obj
'''

file = open('dummy.txt')
print(file.read())
file.close()

f1 = open('radiants.txt','w')
f1.write('The radiant are saviour of humanity')
f1.write('jai shree is a chant to meet your soul')
f1.write('lord rama was purushuttam')
f1.close() # save

f2 = open ('dummy.txt','a')
f2.write('written by SENPAI')
f2.close()