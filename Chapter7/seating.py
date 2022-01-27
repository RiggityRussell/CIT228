#Russell Arlt
#Hands on #1
#Restaurant Seating
print("------------------------Exercise 7-2------------------------")

people = input("How many people are dining tonight?")
if int(people) <= 8:
    print("Your table is ready!")
elif int(people) > 8:
    print("You will have to wait for a table.")
