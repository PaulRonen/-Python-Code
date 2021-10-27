#parent class or super class
class Item:
    def __init__(self,color,material):
        self.color = color
        self.material=material


#child class or sub class
class PhysicalItem(Item):
    def __init__(self, color, material,weight,height,width):
        super().__init__(color, material)
        self.weight = weight
        self.height=height
        self.width=width

#subclass od pgysical item
class SpPhysicalItem (PhysicalItem):
    def __init__(self, color, material, weight, height, width,brand,tech):
        super().__init__(color, material, weight, height, width)
        self.brand=brand
        self.tech=tech

i = Item('red','steel')
j=PhysicalItem('yellow','wood',2,2,3)
k = SpPhysicalItem('yellow','wood',2,2,'plywood')

print(i,j,k)