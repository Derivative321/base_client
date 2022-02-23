
class User:
    def __init__(self):
        self.email = ""
        self.name = ""
        self.password = ""

    def change_password(self, password):
        self.password = password
