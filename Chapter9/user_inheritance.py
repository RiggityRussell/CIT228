#Russell Arlt
#Hands on #3

print("-----------------------Exercise 9-7/9-8-----------------------")

class User:
    def __init__(self, first_name, last_name, age, height):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.height = height
        self.login_attempts = 0
    def increment_login_attempts(self, login):
        self.login_attempts += login
    def reset_login_attempts(self):
        self.login_attempts = 0
    def write_login(self):
        print(f"{self.login_attempts} log attempts")
    
class Admin(User):
    def __init__(self, first_name, last_name, age, height):
        super().__init__(first_name,last_name,age, height)
        self.privileges = Privileges()
    
class Privileges:
    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user", "full access"]
    def show_privileges(self):
        for x in self.privileges:
            print(x)

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

