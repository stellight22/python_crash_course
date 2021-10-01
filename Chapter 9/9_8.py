#9-8 Privileges class

class Privileges():
    def __init__(self, privilege = ['can add user', 'can remove user', 'can ban user', 'can look up user stats']):
        self.privilege = privilege

    def show_privileges(self):
        for ability in self.privilege:
            print(ability)

class User():
    def __init__(self, f_name, l_name, level, life):
        self.f_name = f_name
        self.l_name = l_name
        self.level = level
        self.life = life


    def describe_user(self):
        print("\nFull name: "+ self.f_name.title()+ " "+ self.l_name.title())
        print("Level: "+ str(self.level))
        print("Health: "+ str(self.life))

class Admin(User):
    def __init__(self, f_name, l_name, level, life):

        super().__init__(f_name, l_name, level, life)
        self.privilege = Privileges()
    

admin234 = Admin('Emma', 'Watson', 33, 44)
admin234.describe_user()
admin234.privilege.show_privileges()
