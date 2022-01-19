# Russell Arlt Lesson 2

import random

print("--------------------Hands on 1--------------------")
foodList = ["Pizza", "Potato Tacos", "Buffalo Cauliflower Bites", "Salad", "Quiche", "Pasta"]
print(f"Favorite Foods : {foodList}")
numberList = [1,24,13,70,100,8]
print(f"Lucky Numbers : {numberList}")
movieList = ["I Love You Man", "The Departed", "SpiderMan"]
print(f"Favorite Movies : {movieList}")
randomComboList = [ random.choice(foodList), random.choice(foodList), random.choice(numberList), random.choice(numberList), random.choice(movieList), random.choice(movieList)]
print(f"Random Combo List : {randomComboList}")
print(f"Last Food Item : {foodList[-1]}")
print(f"2nd, 4th, and 6th Numbers : {numberList[1]}, {numberList[3]}, {numberList[5]}")
print(f"All Movies = {movieList[0]}, {movieList[1]}, and {movieList[2]}")
print(f"First Food, Number, and Movie = {randomComboList[0]}, {randomComboList[2]}, {randomComboList[4]}")

print("--------------------Hands on 2--------------------")
movieList.append("The Wedding Singer")
print(f"Added Movie : {movieList}")
numberList.insert(3, 333)
print(f"Added Number At Sub 3 : {numberList}")
foodList.insert(5, "Black Bean Burger")
print(f"Added Food At Sub 5 : {foodList}")
del foodList[6]
print(f"Deleted Food[6] : {foodList}")
numberList.pop(0)
print(f"Deleted First Number : {numberList}")
numberList.pop(2)
print(f"Deleted Number At Sub 2 : {numberList}")

print("--------------------Hands on 3--------------------")
movieList.sort()
print(f"Sorted List : {movieList}")
print(f"Sorted Food List : {sorted(foodList)}")
print(f"Temporary Sorted List : {sorted(numberList)}")
print(f"Unsorted List : {numberList}")
movieList.reverse()
print(f"Movies Sorted in Reverse : {movieList}")

print("--------------------Chapter 4 Hands on 1--------------------")

print("--------------------Food List---------------------")
for x in foodList:
    print(x)

print("--------------------Number List---------------------")
for x in numberList:
    print(x)

print("--------------------Movie List---------------------")
for var in movieList:
    print(var)

print("--------------------Combo List---------------------")
for cccccombo in randomComboList:
    print(cccccombo)