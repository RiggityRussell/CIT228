#Russell Arlt
#Hands on #4

from restaurant import Restaurant
from icecream import IceCreamStand

iceCreamList = ["Vanilla", "Chocolate", "Double Chocolate Sea Salt Caramel"]
flavorTown = IceCreamStand("Bill's Ice Cream Emporium!", "That yummy cold stuff!", iceCreamList)
def food(flavorTown):
    print(f"{flavorTown.name} serves {flavorTown.cuisine}, and has served {flavorTown.number_served} customers!")

food(flavorTown)
flavorTown.FlavorTown()