#Russell Arlt
print("-------------------Exercise 5-1-------------------")
print("-------------------True Results-------------------")
hat = "Top Hat"
print("Is hat == 'Top Hat'? I predict True.")
print(hat == "Top Hat")
cat = "Top Cat"
print("Is cat == 'Top Cat'? I predict True.")
print(cat == "Top Cat")
pickledAsparagus = "Delicious"
print("Is pickledAsparagus == 'Delicious'? I predict True.")
print(pickledAsparagus == "Delicious")
large = 100
print("Is large != '1'? I predict True.")
print(large != 1)
num = 5
print("Is num == '5'? I predict True.")
print(num == 5)
print()
print("-------------------False Results-------------------")
hat = "Top Hat"
print("Is hat == 'Bottom Hat'? I predict False.")
print(hat == "Bottom Hat")
cat = "Top Cat"
print("Is cat != 'Top Cat'? I predict False.")
print(cat != "Top Cat")
pickledAsparagus = "Delicious"
print("Is pickledAsparagus == 'GROSS'? I predict False.")
print(pickledAsparagus == "GROSS")
large = 100
print("Is large == '100'? I predict False.")
print(large == 1000)
num = 5
print("Is num != '5'? I predict False.")
print(num != 5)
print()
print("-------------------Exercise 5-2-------------------")
happy = "Russell is happy today"
print("Is Russell happy today?")
print(happy == "Russell is happy today")
print("Is Russell sad today?")
print(happy != "Russell is happy today")
upper = "THIS STATEMENT IS IN ALL CAPS"
print(f"Is: {upper}?")
print(upper == "THIS STATEMENT IS IN ALL CAPS")
print(f"Is: {upper.lower()}?")
print(upper.lower() == "THIS STATEMENT IS IN ALL CAPS")
numberTime = 100
print(f"Is {numberTime} == 100?")
print(numberTime == 100)
print(f"Is {numberTime} == 500?")
print(numberTime == 500)
num2 = 50
num3 = 500
print(f"Is {numberTime} > {num2}?")
print(numberTime > num2)
print(f"Is {numberTime} > {num3}?")
print(numberTime < num3)
print(f"Is {numberTime} >= {num2}?")
print(numberTime >= num2)
print(f"Is {numberTime} <= {num2}?")
print(numberTime <= num2)
print(f"Is {num2} < {numberTime} and < {num3}?")
print(num2 < numberTime and num2 < num3)
print(f"Is {numberTime} < {num3} or < {num2}?")
print(numberTime < num3 or numberTime < num2)
list = [1,2,3,4,5]
print(f"Is the number 6 in this list? {list}")
print(6 in list)
print(f"Is the number 6  NOT in this list? {list}")
print(6 not in list)
