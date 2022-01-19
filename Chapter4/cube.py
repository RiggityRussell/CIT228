#Russell Arlt
print("-------------------Exercise 4-8-------------------")
cubeList = [1**3, 2**3, 3**3, 4**3, 5**3, 6**3, 7**3, 8**3, 9**3, 10**3]
for cube in cubeList:
    print(cube)
print()
print("-------------------Exercise 4-9-------------------")
cubeCompList = [number**3 for number in range(1,11)] #List comprehension is something I need to practice more.
print(cubeCompList)