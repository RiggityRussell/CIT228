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