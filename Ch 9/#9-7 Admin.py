#9-7 Admin

class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts =0

    def describe_user(self):
        print(self.first_name)
        print(self.last_name)
    
    def greet_user(self):
        print("Hello, " + self.first_name.title() + " "+ self.last_name.title())
    
    def increment_login_attempts(self, num_logins):
        self.login_attempts += num_logins

    def reset_login_attempts(self):
        self.login_attempts = 0

    def show_logins(self):
        print(self.login_attempts)

class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__( first_name, last_name)
        self.privileges ="add mods"

        #from class Privileges
        super().__init__(first_name, last_name)
        self.priv = Privileges()
    
    def show_privileges(self):
        print(self.first_name+" "+ self.last_name + " can " + self.privileges )



class Privileges():
    def __init__(self, privilege = " "):
        self.privilege = " "
    
    def describe_privilege(self):
        print("This Admin can "+ str(self.privilege) + " features in the system like a boss")



Admin1 = Admin('Rocky', 'Handsome')
Admin1.show_privileges()
priv2 = Privileges()
priv2.privilege = "kill"
priv2.describe_privilege()

