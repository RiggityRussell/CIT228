#Russell Arlt
print("-------------------Exercise 5-8-------------------")
adminList = ["admin", "Adam", "Micajah", "Wayne", "Crumbob"]
for user in adminList:
    if user == "admin":
        print(f"Hello {user}, would you like to see a status report?")
    else:
        print(f"Hello {user}, thank you for logging in again")
print()
print("-------------------Exercise 5-9-------------------")
adminList = []
if adminList:
    for user in adminList:
        if user == "admin":
            print(f"Hello {user}, would you like to see a status report?")
        else:
            print(f"Hello {user}, thank you for logging in again")
else:
    print("We need to find some users!")