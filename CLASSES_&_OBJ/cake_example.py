# we have to make class for storing information about cake

class Cake:
    brand = "JJ Bakery"
    flavour = "Chocolate"
    weight = 1
    is_eggless = True
    color = 'brown'


Cake1=Cake()    #object 1
Sasta_Cake=Cake()   #object 2

print(Cake1.flavour)
Sasta_Cake.brand='Chandu bakery'
Sasta_Cake.is_eggless=False
Sasta_Cake.flavour='Strawberry'
Sasta_Cake.color='pink'
Sasta_Cake.weight=.25
print(Sasta_Cake.flavour)

# redundant coding
# lengthy lines
# solution -> intro to construction