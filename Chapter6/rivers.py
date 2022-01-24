#Russell Arlt
#Hands on #2
print("-------------------Exercise 6-5-------------------")
riverDict = {"Volga" : "Russia", "Yangtze" : "China", "Lena" : "Russia"}
for key,value in riverDict.items():
    print(f"The {key} river runs through {value}.")
for key in riverDict.keys():
    print(f"River: {key}")
for value in riverDict.values():
    print(f"Country: {value}")
