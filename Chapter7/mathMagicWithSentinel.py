import random

numProb = int(input("How many math problems would you like to practice?"))
counter = 0
correct = 0
while True:
    addOrSub = input("Would you like to add or subtract?").lower()
    if addOrSub == "add":
        while counter < numProb:
            randNum1 = random.randrange(1,1000)
            randNum2 = random.randrange(1,1000)
            correctAnswer = int(randNum1 + randNum2)
            yourAnswer = int(input(f"what is the integer value of {randNum1} + {randNum2}? "))
            if correctAnswer == yourAnswer:
                print("You got it!")
                correct +=1
            else:
                print(f"Incorrect! the correct answer is {correctAnswer}")
            counter += 1
    elif addOrSub == "subtract":
        while counter < numProb:
            randNum1 = random.randrange(1,1000)
            randNum2 = random.randrange(1,1000)
            correctAnswer = int(randNum1 + randNum2)
            yourAnswer = int(input(f"what is the integer value of {randNum1} + {randNum2}? "))
            if correctAnswer == yourAnswer:
                print("You got it!")
                correct +=1
            else:
                print(f"Incorrect! the correct answer is {correctAnswer}")
            counter += 1
    else:
        print("Please enter only add or subtract")
    break
print(f"You got {correct} answers correct!")
print("Ok bye bye!")