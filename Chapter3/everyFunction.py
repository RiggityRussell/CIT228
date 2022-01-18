#Russell Arlt
from audioop import reverse


colorList = ["Red", "Blue", "Yellow", "Black", "Orange", "Brown", "Green", "Purple", "Gray"]
print(f"The colors in the list are {colorList}")
message = f"The first color in the list is {colorList[0]}"
print(message)
print("We better add Taupe!")
colorList.append("Taupe")
print(f"Proof! {colorList}")
print("I love yellow! Lets put it in again at the beginning!")
colorList.insert(0, "Yellow")
print(f"Proof! {colorList}")
print("OK thats too much yellow.")
del colorList[0]
print(f"Proof! {colorList}")
holdColor = colorList.pop(4)
print(f"I stole a color from the list! {holdColor}")
print(f"Proof! {colorList}")
colorList.remove("Green")
print("I stole another color!")
print(f"Proof! {colorList}")
print(f"Lets make this look nicer {sorted(colorList)}")
colorList.reverse()
print(f"Now reverse the original list! {colorList}")
colorList.sort()
print(f"Now permanently sort that list! {colorList}")
colorList.reverse()
print(f"Now we reverse that list! {colorList}")
print(f"The length of the list is {len(colorList)}")
