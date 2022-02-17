#Russell Arlt
#Hands on #2
import random
import os
"""file = "Chapter10/file.txt"

print("-----------------------Exercise 10-3/4-----------------------")

while True:
    name = input("What is your name?")
    if name == "":
        print("You need to enter a name please. Press enter to continue")
        input()
        continue
    else:
        name = name.title()
        break
with open(file, 'a') as guestFile:
    guestFile.write("Welcome to the Inn " + name + "\n")
with open(file) as file:
    file = file.read()
print(file)
"""


file = "Chapter10/file.txt"
if os.path.exists(file):
    os.remove(file)
boatList = []
boattime = True
with open(file, "w") as boatFile:
    while boattime == True:
        while True:
            name = input("What is your name? ")
            if name == "":
                print("You need to enter a name please. Press enter to continue")
                input()
                continue
            else:
                name = name.title()
                break
        ranNum = random.randint(1,50)
        while ranNum in boatList:
            ranNum = random.randint(1,50)
        boatList.append(ranNum)
        name+= " you have been assigned to boat #" + str(ranNum)
        boatFile.write(name + "\n")
        yOrN = input("Assign another person to a boat? Y/N: ")
        if yOrN.lower() == "y" or yOrN.lower() == "yes":
            print("perfect")
            boattime = True
        else:
            boattime = False
print()
with open(file) as boatFile:
    for x in boatFile:
        print(x)