
class Dog:

    def __init__(self,breed,color,height,name):
        self.breed = breed
        self.color = color
        self.height = height
        self.name = name



Dog1 = Dog('husky','white','150cm','nori')
Dog2 = Dog('greatden','brown','160cm','jango')
Dog3 = Dog('pug','black','30cm','raja')
Dog4 = Dog('desi kutta','multicolor','150cm','tommy')

print(Dog1.name,Dog1.breed)
print(Dog2.name,Dog2.breed)
print(Dog3.name,Dog3.breed)
print(Dog4.name,Dog4.breed)
