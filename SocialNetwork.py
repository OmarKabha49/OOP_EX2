from user import User


# SocialNetwork class implementing Singleton pattern
class SocialNetwork:
    _instance = None

    # Singleton implementation in __new__ method
    def __new__(cls, name=str):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    # Constructor to initialize the social network
    def __init__(self, name=str):
        if not hasattr(self, 'name'):
            self.name = name
            self.Users = []  # List to hold users
            print(f"The social network {name} was created!")

    # Method for user sign up
    def sign_up(self, userName=str, passWord=str):
        user = User(userName, passWord)
        if user not in self.Users:
            self.Users.append(user)
            user.isOnline = True
        return user

    # Method for user log out
    def log_out(self, username=str):
        for user in self.Users:
            if user.username == username:
                user.isOnline = False
                print(f"{user.username} disconnected")

    # Method for user log in
    def log_in(self, userName=str, passWord=str):
        for user in self.Users:
            if user.username == userName and user.password == passWord:
                user.isOnline = True
                print(f"{user.username} connected")

    # Method to return string representation of the social network
    def __str__(self):
        network_str = f"{self.name} social network:\n"
        for user in self.Users:
            network_str += str(user) + "\n"
        return network_str[:-1]
