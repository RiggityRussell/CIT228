import json
import matplotlib.pyplot as plt

# file = 'vizualization_project/data/FoodData.json'
# with open(file, encoding='utf8') as f:
#     sig_quake = json.load(f)

# readable_file = 'vizualization_project/data/readableFoodData.json'
# with open(readable_file, 'w') as quakey:
#     json.dump(sig_quake, quakey, indent=4)

file = 'vizualization_project/data/readableFoodData.json'
with open(file) as f:
    food_data = json.load(f)

foods = food_data['FoundationFoods']

iron_food, iron =[], []
energy_Atwater, energy_food = [], []
pufa, pufa_food = [], []
SFA, SFA_food= [], []
calcium, calcium_food = [], []
Water, Water_food = [], []

for food in foods:
    if food['foodNutrients'][0]['nutrient']['name'] == "Iron, Fe":
        var = food['description']
        var2 = food['foodNutrients'][0]['nutrient']['name']
        iron_food.append(var)
        iron.append(var2)
    elif food['foodNutrients'][0]['nutrient']['name'] == "Energy (Atwater Specific Factors)":
        var = food['description']
        var2 = food['foodNutrients'][0]['nutrient']['name']
        energy_food.append(var)
        energy_Atwater.append(var2)
    elif food['foodNutrients'][0]['nutrient']['name'] == "PUFA 22:5 n-3 (DPA)":
        var = food['description']
        var2 = food['foodNutrients'][0]['nutrient']['name']
        pufa_food.append(var)
        pufa.append(var2)
    elif food['foodNutrients'][0]['nutrient']['name'] == 'SFA 4:0':
        var = food['description']
        var2 = food['foodNutrients'][0]['nutrient']['name']
        SFA_food.append(var)
        SFA.append(var2)
    elif food['foodNutrients'][0]['nutrient']['name'] == 'Calcium, Ca':
        var = food['description']
        var2 = food['foodNutrients'][0]['nutrient']['name']
        calcium_food.append(var)
        calcium.append(var2)
    elif food['foodNutrients'][0]['nutrient']['name'] == 'Water':
        var = food['description']
        var2 = food['foodNutrients'][0]['nutrient']['name']
        Water_food.append(var)
        Water.append(var2)

labels = 'Iron, Fe', 'Energy (Atwater Specific Factors)', 'PUFA 22:5 n-3 (DPA)', 'SFA 4:0', 'Calcium, Ca', 'Water'
num_of_nutrients = (len(iron_food), len(energy_food), len(pufa_food), len(SFA_food), len(calcium_food), len(Water_food))
explode = (0,0,0,0,0,.10)

fig1, ax1 = plt.subplots()
ax1.pie(num_of_nutrients, explode = explode, labels=labels, autopct='%3.1f%%', shadow=True, startangle = 5)
ax1.axis('equal')
plt.suptitle('Food Nutrient percentages for 147 sampled foods')

for food in iron_food:
    print(food)
for food in energy_food:
    print(food)
for food in pufa_food:
    print(food)
for food in SFA_food:
    print(food)
for food in calcium_food:
    print(food)
for food in Water_food:
    print(food)

num = (len(iron_food) + len(energy_food) + len(pufa_food) + len(SFA_food) + len(calcium_food) + len(Water_food))
print(num)
plt.show()





