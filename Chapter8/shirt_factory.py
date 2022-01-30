#Russell Arlt
from re import S, X


print("-----------------------Exercise 8-3-----------------------")
def make_shirt(size,text):
    print(f"The size of the shirt is {size.upper()}, and the text on it is {text}!")

sizeList = ["S","M","L","XL"]
while(True):
    size = input("What size shirt?(S,M,L,XL): ")
    if size.upper() not in sizeList: 
        print("Whoopsie Do! Better try again.")
    else:
        break
while(True):
    text = input("What would you like the shirt to say?: ")
    if text == "":
        yOrN = input("Are you sure you want a blank shirt?: ")
        if yOrN.lower() == "yes":
            print("Okie Dokie!")
            break
        else:
            print("Lets try again.")
            continue
    else:
        break

make_shirt(size,text)

print("-----------------------Exercise 8-4-----------------------")

def make_shirt(size):
    if size.upper() == "M" or size.upper() == "L":
        print(f"The size of the shirt is {size.upper()}, and the text on it is I love Python!")
    elif size.upper() == "S":
        print(f"The size of the shirt is {size.upper()}, and the text on it is I like Turtles!")
    else:
        print(f"The size of the shirt is {size.upper()}, and the text on it is I have entered the else area!")

while(True):
    sizeList = ["S","M","L","XL"]
    while(True):
        size = input("What size shirt?(S,M,L,XL): ")
        if size.upper() not in sizeList: 
            print("Whoopsie Do! Better try again.")
        else:
            break


    make_shirt(size)
    yOrN = input("would you like to get another shirt?: ")
    if yOrN.lower() == "yes":
        print("Okie Dokie!")
        continue
    else:
        print("OK! Bye bye!")
        break
