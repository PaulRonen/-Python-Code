
class IceCreme:

    def __init__(self,flovor,price,brand,style):
        self.flovor = flovor
        self.price = price
        self.brand = brand
        self.style = style



#object

ic1 = IceCreme('chocolate',30,'Vadilal','bar')
ic2 = IceCreme('sitafal',60,'Gaini','Cup')

print(ic1.brand,ic1.flovor)
print(ic2.brand,ic2.flovor)