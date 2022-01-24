#Russell Arlt
#Hands on #3

print("-------------------3 Dictionaries in a list-------------------")
bookDict = {"Recently Read" : "The Blacktongue Thief", "Favorite Book" : "The Magicians"}
gameDict = {"Newest Board Game" : "Dune Imperium", "Favorite Board Game" : "Terraforming Mars"}
musicDict = {"New Music" : "Birdy", "Favorite Artist" : "Sam Lynch"}

dictList = [bookDict, gameDict, musicDict]
for dict in dictList:
    print(dict)