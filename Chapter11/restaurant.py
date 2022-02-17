#Russell Arlt
#Hands on #2

class Restaurant():
    def __init__(self, restaurant_name, cuisine_type, number_served = 0):
        self.name = restaurant_name
        self.cuisine = cuisine_type
        self.number_served = number_served
    def set_number_served(self, custos):
        self.number_served = custos
    def increment_number_served(self, increase):
        self.number_served = self.number_served + increase