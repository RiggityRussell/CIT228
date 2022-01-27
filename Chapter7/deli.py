#Russell Arlt
print("--------------------Exercise 7-8--------------------")
sandwich_orders = [
    "Hummus", 
    "Pastrami",
    "Portobella Mushroom", 
    "Pastrami",
    "Curried Chickpea", 
    "Tomato Pesto", 
    "Pastrami",
    "Peanut Butter and Jelly",
    "Grilled Cheese"]
finished_sandwiches = []

#for sandwich in sandwich_orders:
   # print(f"I made your {sandwich} sandwich")

#while sandwich_orders:
   # heldVar = sandwich_orders.pop()
   # finished_sandwiches.append(heldVar)
#print("Sandwiches that were made today:")
#for sandwich in finished_sandwiches:
    #print(sandwich)

print("--------------------Exercise 7-9--------------------")
print("We are out of pastrami today, apologies for the inconvenience.")
while "Pastrami" in sandwich_orders:
    sandwich_orders.remove("Pastrami")
for sandwich in sandwich_orders:
    print(f"I made your {sandwich} sandwich")

while sandwich_orders:
    heldVar = sandwich_orders.pop()
    finished_sandwiches.append(heldVar)
print("Sandwiches that were made today:")
for sandwich in finished_sandwiches:
    print(sandwich)