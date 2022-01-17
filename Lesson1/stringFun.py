# exercise 1 - Russell Arlt
print("---------------------------------------")
print("Exercise 1")
name = "russell arlt" #creating variable of my name
print(name.title()) #printing the variable and using a method to capitalize the first letter in both names
print(name.upper()) #printing the variable and using a method to capitalize all letters in both names
print(name.lower()) #printing the variable and using a method to make all letters lowercase
print(f"My first initial is: {name[0].upper()}") #printing the first letter in the variable name by calling its place (0) and using the upper method to capitalize it.

#exercise 2 - Russell Arlt
print("---------------------------------------")
print("Exercise 2")
noun = "Kitten" 
adj = "sleepy"
verb = "exploded"
ending = "the minds of everyone on the internet."
sentence1 = "The " + adj + " purring " + noun + " " + verb + " " + ending
sentence2 = f"The {adj} purring {noun} {verb} {ending}"
print(sentence1.upper())
print(sentence2.lower())

#exercise 3 - Russell Arlt
print("--------------------------------------")
print("Exercise 3") 
longExerpt = """Shadow had done three years in prison. 
\tHe was big enough, and looked don't-mess-with-me enough
that his biggest problem was killing time.
\tSo he kept himself in shape, and taught himself coin tricks,
and thought a lot about how much he loved his wife.
""" # above, the triple quotations allows us to create a string value on multiple lines. Also using the \ character (move past character in this case) to create a tab effect in the string.
print(longExerpt)

#exercise 4 -Russell Arlt
print("-------------------------------------")
print("Exercise 4")
print("Hello\tLisa\nI\tdidn't\nrealize\tthis\nclass\tstarted\nwith\tPython!") #using \t to create a tab effect, and \n to create a newline effect.
