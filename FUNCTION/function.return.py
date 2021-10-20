def hypotenuse(p,b):
    hyp = (p** +b**2) **.5
    return hyp

#ans can be stored
ans = hypotenuse(3,4)
print('answer',ans)

#can be used in expression
out = hypotenuse(3,4 )  + hypotenuse (4,3)  * 5
print(out)

#can be directly printed if no variable is needed
print(hypotenuse(10,10))

