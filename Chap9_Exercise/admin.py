from user import User

class Admin(User):
    """Special user"""

    def __init__(self, first_name, last_name) -> None:
        """Initialize like the normal user but have the privilege"""
        super().__init__(first_name, last_name)
        # self.privilege  = ['can add post', 'can delete post', 'can ban user']
        self.privilege      = Privilege()

    # def show_privilege(self):
    #     """Show all the privilege of the admin user"""
    #     print("-------- Admin privilege ---------")
    #     for action in self.privilege:
    #         print(f"-{action}")

class Privilege:
    """Sub class to separate the privilege function"""

    def __init__(self) -> None:
        """Initialize only the privilege actions"""
        self.privilege  = ['can add post', 'can delete post', 'can ban user']
    
    def show_privilege(self):
        """Show all the privilege of the admin user"""
        print("-------- Admin privilege ---------")
        for action in self.privilege:
            print(f"-{action}") 

# my_user     = User('Pattarapol', 'Sangaroon')
# my_user.describe_user()
# my_user.greet_user()

# my_user.increase_login_attempt(20)
# my_user.reset_login_attempt()
# print('\n')

# my_admin    = Admin('Pat', 'Sang')
# my_admin.greet_user()
# # my_admin.show_privilege()

# my_admin.privilege.show_privilege()