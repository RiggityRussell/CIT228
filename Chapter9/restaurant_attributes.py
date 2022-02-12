#Russell Arlt
#Hands on #2

print("-----------------------Exercise 9-4-----------------------")

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.cuisine = cuisine_type
        self.number_served = 0
    def set_number_served(self, custos):
        self.number_served = custos
    def increment_number_served(self, increase):
        self.number_served += increase
        

restaurant = Restaurant("Dales Sandwich Alley", "Sloppy Sandwiches")
def rezz(restaurant):
        print(f"{restaurant.name} serves {restaurant.cuisine}, and has served {restaurant.number_served} customers!")
rezz(restaurant)
restaurant.number_served = 1000
rezz(restaurant)
restaurant.set_number_served(5000)
rezz(restaurant)
restaurant.increment_number_served(30)
rezz(restaurant)



