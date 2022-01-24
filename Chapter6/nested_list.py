#Russell Arlt
#Hands on #3


print("-------------------1 Dictionary with a list-------------------")
listDict = {
                "Favorite Candies" : ["Sea Salt Chocolate Caramels", "Kit Kats", "Mounds", "Almond Joy"], 
                "Favorite Cakes" : ["Tres Leches", "Tiramisu", "Red Velvet"]
           }

for key, value in listDict.items():
    print(f"These are my {key}: {value}")