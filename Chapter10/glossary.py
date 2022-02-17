#Russell Arlt
#Hands on #1

import json

def UserChoice():
    while True:
        try:
            choice = int(input(
                """Enter 1 to create the glossary json file
Enter 2 to read from the glossary and print the glossary 
Enter 3 to add to the glossary json file
Enter 4 to quit the application
"""))
            return choice
        except ValueError:
            print("Enter a number between 1 and 4 and press the enter key please.")
            continue

def Create(glossaryDict):
    overwrite = input("You are about to create a new file, existing data will be overwritten (q to quit, any key to continue) ")
    if overwrite !="q":
        with open("Chapter10/glossary.json", "w") as write_file:
            json.dump(glossaryDict, write_file, indent=4, sort_keys=True)
            print("glossary.json has been created")

def Read():
    try:
        with open("Chapter10/glossary.json") as read_file:
            numberDictionary = json.load(read_file)
    except FileNotFoundError:
        print("The file doesn't exist or cannot be found.")
        print("Please make a different menu selection")      
    else: 
        for key, value in numberDictionary.items():
            print(f"{key.title()} can be explained as such: {value}")

def GetWord():
    word = input("Enter a programming word!\n")
    word = word.lower()
    return word

def GetDef(word):
    definition = input(f"Enter a definition for {word}\n")
    definition = definition.lower()
    return definition

def append(keyValue):
    with open("Chapter10/glossary.json", "r+") as add_file:
        addDictionary = json.load(add_file)
        addDictionary.update(keyValue)
        add_file.seek(0)
        json.dump(addDictionary, add_file, indent=4, sort_keys=True)
        print("Data has been added to numbers.json")

glossaryDict = {
    "if-statement" : "if statements are used to determine equality, comparisons, and conditions.",
    "List" : "A group of elements that can be accessed by their numerical value within the list.",
    "Boolean expression" : "A conditional test to determine if something is True or False.",
    "Tuple" : "A list of items that cannot be changed.",
    "in/ not in" : "Checks to see if there is an equivalent value in, or not in, a list or condition.",
    "Comments" : "comments are denoted with a hastag, #, and the texst after it is not compiled by the program.",
    "Constant" : "variable whose value stays the same throughout the program.",
    "Float" : "Any number with a decimal point.",
    ".strip" : "Strips extra white space from both sides of a string, or other variable type.",
    "Variable" : "Holder of a value"
                }
while True:
    choice = UserChoice()
    if choice == 1:
        Create(glossaryDict)
        continue
    elif choice == 2:
        Read()
        continue
    elif choice == 3:
        word = GetWord()
        definition = GetDef(word)
        keyValue = {word:definition}
        append(keyValue)
        continue
    elif choice == 4:
        break
    else:
        print("INVALID.")
        continue