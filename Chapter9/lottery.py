#Russell Arlt
#Extra Credit!
from random import randint
from random import choice

print("-----------------------Exercise 9-14-----------------------")

lotto = [1,2,5,8,3,14,13,24,80,4,"a","r","l","t","s"]
lottoBotto = []
x = 0
while(True):
    if x < 4:
        zip = choice(lotto)
        lottoBotto.append(zip)
        x += 1
    else:
        break

print("If your ticket matches the following numbers and letters you win!")
print(lottoBotto)