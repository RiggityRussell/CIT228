#Russell Arlt
print("------------------------Exercise 3-4------------------------")
people_list = ["Greg", "Mitch Hedberg", "Micajah"]
to_dinner = "would you like to come to dinner?"

for person in people_list:
    print(person, to_dinner)
print()
print("------------------------Exercise 3-5------------------------")
people_list = ["Greg", "Mitch Hedberg", "Micajah"]
to_dinner = "would you like to come to dinner?"

for person in people_list:
    print(person, to_dinner)
print("Greg cannot make it.")
people_list.remove("Greg")
people_list.append("The Great Wizard Balthatrol")
for person in people_list:
    print(person, to_dinner)
print()
print("------------------------Exercise 3-6------------------------")
print("I have procured a larger table, we now can invite more people!")
people_list.insert(0, "Rick")
people_list.insert(3, "Morty")
people_list.append("Greg Jr.")
for person in people_list:
    print(person, to_dinner)
print("------------------------Exercise 3-9------------------------")
print(f"The number of people on my guest list is : {len(people_list)}")
print("------------------------Exercise 3-7------------------------")
print("My table is not here yet. I AM SAD. Only 2 guests may come to dinner.")
print(f"{people_list.pop(0)} I am sorry to inform you dinner is canceled.")
print(f"{people_list.pop(0)} I am sorry to inform you dinner is canceled.")
print(f"{people_list.pop(1)} I am sorry to inform you dinner is canceled.")
print(f"{people_list.pop(2)} I am sorry to inform you dinner is canceled.")
print()
for person in people_list:
    print(person, to_dinner)
del people_list[0]
del people_list[0]
print(f"My guest list is empty now as sad as I am: {people_list}")