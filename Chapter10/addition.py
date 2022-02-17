#Russell Arlt
#Hands on #3
print("-----------------------Exercise 10-6/10-7-----------------------")

while True:
    try:
        int1 = int(input("Please enter an integer: "))
        break
    except:
        ValueError
        continue
while True:
    try:
        int2 = int(input("Please enter an integer: "))
        break
    except:
        ValueError
        continue

print(f"The value of those integers added together is: {int1 + int2}")








