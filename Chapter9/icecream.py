#Russell Arlt
#Hands on #4

from restaurant import Restaurant

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type,)
        self.name = restaurant_name
        self.cuisine = cuisine_type
        self.number_served = 0
        self.flavors = flavors

    def FlavorTown(self):
        print("Here's a list of flavors!")
        for flavor in self.flavors:
            print(flavor)