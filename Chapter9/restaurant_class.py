#Russell Arlt
#Hands on #1

print("-----------------------Exercise 9-1-----------------------")

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.cuisine = cuisine_type
    
r = Restaurant("The Good Bowl", "Vietnamese")
def describe_restaurant(r):
        print("Restaurant = " + r.name)
        print("Cuisine = " + r.cuisine)   

def open_restaurant(self):
        print(f"{self.name} is open.") 

describe_restaurant(r)
open_restaurant(r)

my_rest = Restaurant("Hamtown", "Ham")

print(f"{my_rest.name} is where we get {my_rest.cuisine}")
describe_restaurant(my_rest)
open_restaurant(my_rest)

print("-----------------------Exercise 9-2-----------------------")

restaurant_one = Restaurant("Bubbas", "American")
restaurant_two = Restaurant("Hunan", "Chinese")
restaurant_three = Restaurant("Spanglish", "Mexican")
describe_restaurant(restaurant_one)
describe_restaurant(restaurant_two)
describe_restaurant(restaurant_three)

