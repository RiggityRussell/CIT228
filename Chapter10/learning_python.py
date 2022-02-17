#Russell Arlt
#Hands on #1

print("-----------------------Exercise 10-1-----------------------")

file1 = "Chapter10/learning_python.txt"

print("-----------------------read() example-----------------------")
with open(file1) as file2:
    file2=file2.read()
print(file2, "\n")

print("-----------------------for loop example-----------------------")
with open(file1) as file2:
    for x in file2:
        print(x.rstrip())
print()
print("-----------------------readlines example-----------------------")
with open(file1) as file2:
    file2 = file2.readlines()
for x in file2:
    print(x.strip())