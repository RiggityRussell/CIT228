#Russell Arlt
#Hands on #2

print("-----------------------Exercise 8-9-----------------------")
def show_messages1(textList):
    for text in textList:
        print(text)

textList = ["Hello!", "How are you?", "Lets go rock climbing!", "I want pizza."]
show_messages1(textList)

print("-----------------------Exercise 8-10-----------------------")
def show_messages2(textList):
    sent_messages = []
    print("List from textList:")
    for text in textList:
        print(text)
    while textList:
        var = textList.pop()
        sent_messages.append(var)
    return sent_messages
sent_messages = show_messages2(textList) 
print(textList)
print("List from sent_messages:")
for text in sent_messages:
    print(text)

print("-----------------------Exercise 8-11-----------------------")

def show_messages3(textList):
    sent_messages = []
    for text in textList:
        print(text)
    print()
    while textList:
        var = textList.pop()
        sent_messages.append(var)
    return sent_messages
textList = ["Hello!", "How are you?", "Lets go rock climbing!", "I want pizza."]
sent_messages = show_messages3(textList[:]) 
print("List from textList:")
for text in textList:
    print(text)
print()
print("List from sent_messages:")
for text in sent_messages:
    print(text)

