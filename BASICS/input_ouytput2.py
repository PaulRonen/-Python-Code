a = 10
b = "balls"
c = 100
d ="rupees"

#printing with comma seprated

print("Raju purchased",a,b,"for",c,d)

#concatenate using+
print('raju purchased  mnjmj '+ str(a) + ' for ' + b + "for "+str(c) + ' ' + d)

#printing formt specifier
print("Raju purchased %d %s for %d %s" %(a,b,c,d))

#print using format{ method}
print("raju purchased {} {} for {} {}".format(a,b,c,d))

#print using f-string{from3,6}
print(f'Raju purchased {a} {b} for {c} {d}')

#propty of print function
# end - handel waht will be displayed after printing content
# sep - seprator symbol

print('hi',end='' )
print('there')

print(a,b,c,d)
print(a,b,c,d, sep='xx')

