class User:
    """A simple user attributes"""

    def __init__(self, first_name, last_name) -> None:
        """Initialize first name and last name"""
        self.first_name     = first_name
        self.last_name      = last_name
        self.login_attempt  = 0

    def describe_user(self):
        """Print the overall describe of this user"""
        print(f"\n------- User Information --------")
        print(f"First name: {self.first_name}")
        print(f"Last name: {self.last_name}\n")
    
    def greet_user(self):
        """Print greeting message to the user"""
        print(f"Hello {self.first_name}, welcome back online!!!!")

    def increase_login_attempt(self, increase = 1):
        """"Increase login attempt with the input"""
        self.login_attempt  += increase
        print(f"Now user {self.first_name} has {self.login_attempt} times.")

    def reset_login_attempt(self):
        """"Reset login attempt to 0"""
        self.login_attempt  = 0
        print(f"Reset login attempt of user {self.first_name}")
        print(f"Now user {self.first_name} has {self.login_attempt} times.")
