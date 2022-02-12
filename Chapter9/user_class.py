#Russell Arlt
#Hands on #1

print("-----------------------Exercise 9-3-----------------------")

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

user = User("Russell", "Arlt", 34, "5'9")
greg = User("Greg", "Gregson", 63, "6'2")
stefen = User("Stefen", "Holtrey", 34, "5'9")
tyler = User("Tyler", "Hsu", 34, "5'8")
micajah = User("Micajah", "Worden", 34, "5'10")


def describe_user(user):
    print(user.first_name)
    print(user.last_name)
    print(user.age)
    print(user.height)

def greet_user(user):
    print(f"Hello {user.first_name} {user.last_name}, I hear you are {user.age} years old, and are {user.height}.")

describe_user(user)
greet_user(user)
describe_user(greg)
greet_user(greg)
describe_user(stefen)
greet_user(stefen)
describe_user(tyler)
greet_user(tyler)
describe_user(micajah)
greet_user(micajah)

print("-----------------------Exercise 9-5-----------------------")

user.increment_login_attempts(1)
user.write_login()
user.increment_login_attempts(1)
user.write_login()
user.increment_login_attempts(1)
user.write_login()
user.increment_login_attempts(1)
user.write_login()
user.reset_login_attempts()
user.write_login()

