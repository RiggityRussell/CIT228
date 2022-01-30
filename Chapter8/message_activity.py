#Russell Arlt
#Hands on #4
#import messages
#import messages as m
#from messages import show_messages1, show_messages2, show_messages3
#from messages import *
from messages import show_messages1 as sm1, show_messages2 as sm2, show_messages3 as sm3


print("-----------------------Exercise 8-15-----------------------")
firstList = ["Left", "Right", "Up", "Down"]
secondList = ["Down", "Up", "Right", "Left"]
thirdList = ["Banana", "Apple", "Orange"]

sm1(firstList)
var = sm2(secondList)
print(secondList)
print("List from var:")
for text in var:
    print(text)
sent_messages = sm3(thirdList[:]) 
print("List from thirdList:")
for text in thirdList:
    print(text)
print()
print("List from sent_messages:")
for text in sent_messages:
    print(text)