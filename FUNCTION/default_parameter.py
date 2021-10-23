def summer2(a,b,c,d=0):
    return a + b + c + d

print(summer2(1,2,3,4))
print(summer2(1,2,3))
print(summer2(a=1,b=2,c=3))
print(summer2(b=12,a=23,c=2,d=4))
print(summer2(c=1,b=2,a=3))
print(summer2(1,2,3,d=3))

#always put default parameter after
#required parameter

def traingle (b=1,h=1):
    return 1/2 * b * h 

print(traingle())
print(traingle(b = 10))
print(traingle(b = 5 , h = 54))
print(traingle(h = 8))
print(traingle(h = 45 , b = 26))
print(traingle(2,3))
print(traingle(2))
print(traingle(3))

