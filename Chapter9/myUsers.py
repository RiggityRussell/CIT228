from user import User
from privileges import Privileges
from admin import Admin



user = Admin("Russell", "Arlt", 34, "5'9")

def describe_admin(user):
    print(user.first_name)
    print(user.last_name)
    print(user.age)
    print(user.height)
    print("-----Admin privileges-----")
    user.privileges.show_privileges()
    
def greet_user(user):
    print(f"Hello {user.first_name} {user.last_name}, I hear you are {user.age} years old, and are {user.height}.")

describe_admin(user)
greet_user(user)