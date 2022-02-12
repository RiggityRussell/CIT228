class Privileges:
    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user", "full access"]
    def show_privileges(self):
        for x in self.privileges:
            print(x)