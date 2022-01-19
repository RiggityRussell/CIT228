current_users = ["Mitchell", "Gritchell", "Stitchell", "Greg", "Russ"]
new_users = ["Pitchell", "Witchell", "Hitchell", "Greg", "Russ"]

for user in new_users:
    if user in current_users:
        print(f"{user}, this name is unavailable. Please enter a new name.")
    else:
        print(f"{user}, this name is available. Great name.")
print()
current_users_lower = []
for user in current_users:
    current_users_lower.append(user.lower())
for user in new_users:
    if user.lower() in current_users_lower:
        print(f"{user}, this name is unavailable. Please enter a new name.")
    else:
        print(f"{user}, this name is available. Great name.")