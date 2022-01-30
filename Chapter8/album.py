#Russell Arlt
#Hands on #2

from tkinter.messagebox import YES


print("-----------------------Exercise 8-7-----------------------")

def make_album(artistName, albumTitle, songNum = 0):
    musicDict = {"Artist Name: " : artistName, "Album Title: ": albumTitle }
    if songNum:
        musicDict["Number of Songs: "] = songNum
    return musicDict


artistName = "Trent Reznor"
albumTitle = "The Fragile"
musicDict = make_album(artistName, albumTitle)
for k,v in musicDict.items():
    print(k,v)
print()


artistName = "Sam Lynch"
albumTitle = "Little Disappearance"
musicDict = make_album(artistName, albumTitle)
for k,v in musicDict.items():
    print(k,v)
print()

artistName = "Birdy"
albumTitle = "Fire Within"
musicDict = make_album(artistName, albumTitle)
for k,v in musicDict.items():
    print(k,v)
print()

artistName = "Maggie Rogers"
albumTitle = "Heard it in a Past Life"
songNum = 12
musicDict = make_album(artistName, albumTitle, songNum)
for k,v in musicDict.items():
    print(k,v)
print()

print("-----------------------Exercise 8-8-----------------------")

back = True
while(True):
    musicDict = {}
    yOrN = input("Would you like to add musician information? ")
    if yOrN.lower() == "yes":
        while(back):
            artistName = input("Please enter artist name. ")
            if artistName == "":
                print("You must enter an artist name. Press any key to try again.")
                input()
                continue
            else:
                musicDict["Artist Name: "] = artistName
                while(back):
                    albumTitle = input(f"Please enter the album for {artistName}: ")
                    if albumTitle == "":
                        print("You must enter an album title. Press any key to try again.")
                        input()
                        continue
                    else:
                        musicDict["Album Title: "] = albumTitle
                        songNum = input("How many songs are on the album? ")
                        break
            break        
        musicDict = make_album(artistName, albumTitle, songNum)
        for k,v in musicDict.items():
            print(k,v)
        print()

    else:
        print("Ok! Bye bye!")
        break

