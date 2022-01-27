import random


print("MATH PRACTICE TIME!")
keepPlaying = True
correct = 0
incorrect = 0
while keepPlaying:
    addOrSub = input("Would you like to add or subtract?").lower()
    if addOrSub == "add":
        randNum1 = random.randrange(1,1000)
        randNum2 = random.randrange(1,1000)
        correctAnswer = int(randNum1 + randNum2)
        yourAnswer = int(input(f"what is the integer value of {randNum1} + {randNum2}? "))
        if correctAnswer == yourAnswer:
            print("You got it!")
            correct += 1
        else:
            print(f"Incorrect! the correct answer is {correctAnswer}")
            incorrect += 1
        yOrN = input("Do you want to keep playing?").lower()
        if yOrN == "yes":
            keepPlaying = True
        else:
            keepPlaying = False

    elif addOrSub == "subtract" or addOrSub == "sub":
        randNum1 = random.randrange(1,1000)
        randNum2 = random.randrange(1,1000)
        correctAnswer = int(randNum1 - randNum2)
        yourAnswer = int(input(f"what is the integer value of {randNum1} - {randNum2}? "))
        if correctAnswer == yourAnswer:
            print("You got it!")
            correct += 1
        else:
            print(f"Incorrect! the correct answer is {correctAnswer}")
            incorrect += 1
        yOrN = input("Do you want to keep playing?").lower()
        if yOrN == "yes":
            keepPlaying = True
        else:
            keepPlaying = False
print(f"You got {correct} answers correct!")
print(f"You got {incorrect} answers incorrect!")
print("Ok bye bye!")