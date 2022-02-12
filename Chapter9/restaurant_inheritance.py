#Russell Arlt
#Hands on #3

print("-----------------------Exercise 9-6-----------------------")

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.cuisine = cuisine_type
        self.number_served = 0
    def set_number_served(self, custos):
        self.number_served = custos
    def increment_number_served(self, increase):
        self.number_served += increase
        
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
iceCreamList = ["Vanilla", "Chocolate", "Double Chocolate Sea Salt Caramel"]
flavorTown = IceCreamStand("Bill's Ice Cream Emporium!", "That yummy cold stuff!", iceCreamList)
def food(flavorTown):
    print(f"{flavorTown.name} serves {flavorTown.cuisine}, and has served {flavorTown.number_served} customers!")

food(flavorTown)
flavorTown.FlavorTown()