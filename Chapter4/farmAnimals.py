#Hands on #3 Russell Arlt

original_list = ["chicken", "duck", "horse", "piggy", "alpaca", "yak"]
print("----------------- Original List -----------------")
for animal in original_list:
    print(animal)
slice_list = original_list[:]
slice_list.append("cow")
slice_list.append("goat")
slice_list.append("cat")
slice_list.append("dog")
print("----------------- New List -----------------")
for animal in slice_list:
    print(animal)

print()
print("----------------- 4-10 -----------------")
for animal in slice_list:
    print(animal)
print("The first three items in the list are:")
for item in slice_list[0:3]:
    print(item)
print("The middle three items in the list are:")
for item in slice_list[3:6]:
    print(item)
print("The last three items in the list are:")
for item in slice_list[7:10]:
    print(item)