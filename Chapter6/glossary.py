#Russell Arlt
#Hands on #1
print("-------------------Exercise 6-3-------------------")
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

#print("if statement: \n\t", glossaryDict["if-statement"])
#print("List: \n\t", glossaryDict["List"])
#print("Boolean expression: \n\t", glossaryDict["Boolean expression"])
#print("Tuple: \n\t", glossaryDict["Tuple"])
#print("in/ not in: \n\t", glossaryDict["in/ not in"])

#Hands on #2
print("-------------------Exercise 6-4-------------------")
for key, value in glossaryDict.items():
    print(f"{key}: \n\t{value}")