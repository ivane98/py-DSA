class User:
    def __init__(self, username, name, email) -> None:
        self.username = username
        self.name = name
        self.email = email
        print('User Created')

    def intro_yourself(self, guest_name):
        print(f"Hi {guest_name}, i'am {self.name} contact me at {self.email}")

    def __repr__(self) -> str:
        return f"User(username={self.username}, name={self.name}, email={self.email})"
    
    def __str__(self) -> str:
        return self.__repr__()


user1 = User('john', 'John Doe', 'john@doe.com')
print(user1)
