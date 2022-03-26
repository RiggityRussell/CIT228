import json

import matplotlib.pyplot as plt
import random as rand

file = 'vizualization_project/data/fav_pies.json'
with open(file) as f:
    pie_data = json.load(f)


pies = pie_data["Pies"]["type"]

pie_fruit_list = []
pie_cream_list = []
pie_holiday_list = []

num = 0

while num < (len(pies)):
    for pie in pies:
        if pie['id'] == "fruit":
            pie_fruit_list.append(pie["name"])
        if pie['id'] == "cream":
            pie_cream_list.append(pie["name"])
        if pie['id'] == "holiday":
            pie_holiday_list.append(pie["name"])
        num +=1
for pie in pie_cream_list:
    print(pie)
for pie in pie_fruit_list:
    print(pie)
for pie in pie_holiday_list:
    print(pie)

num = 0
rand_numbers = []
while num < len(pie_fruit_list):
    i = rand.randint(1,10)
    rand_numbers.append(i)
    num +=1
print(rand_numbers)


rate = rand_numbers
fruitPie = pie_fruit_list

plt.bar(fruitPie, rate, color="red", width= .75)

plt.xlabel("Pie names: Fruit")
plt.ylabel("Rated out of 10")
plt.title("Bar graph of some of my favorite pies!")
plt.show()

# rate = rand_numbers
# fruitPie = pie_cream_list

# plt.bar(fruitPie, rate, color="lemonchiffon", width= .75)

# plt.xlabel("Pie names: Cream")
# plt.ylabel("Rated out of 10")
# plt.title("Bar graph of some of my favorite pies!")
# plt.show()

# rate = rand_numbers
# fruitPie = pie_holiday_list

# plt.bar(fruitPie, rate, color="brown", width= .75)

# plt.xlabel("Pie names: Holiday")
# plt.ylabel("Rated out of 10")
# plt.title("Bar graph of some of my favorite pies!")
# plt.show()
