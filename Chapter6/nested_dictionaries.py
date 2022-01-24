#Russell Arlt
#Hands on #3

print("-------------------Nested Dictionary-------------------")
nestDict = {
                "Bungie" : {"Game 1" : "Halo", "Game 2" : "Halo 2", "Game 3" : "Halo 3"},
                "343 Industries" : {"Game 1" : "Halo 4", "Game 2" : "Halo 5 Guardians", "Game 3" : "Halo Infinite"}

           }

for key, value in nestDict.items():
    print(f"\nDeveloper: {key}")
    g1 = value["Game 1"]
    g2 = value["Game 2"]
    g3 = value["Game 3"]


    print(f"\tGame 1: {g1}")
    print(f"\tGame 2: {g2}")
    print(f"\tGame 3: {g3}")
