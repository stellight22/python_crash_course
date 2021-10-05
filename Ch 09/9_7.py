#9-7 class Admin

class User():
    def __init__(self, f_name, l_name, level, life):
        self.f_name = f_name
        self.l_name = l_name
        self.level = level
        self.life = life


    def describe_user(self):
        print("Full name: "+ self.f_name.title()+ " "+ self.l_name.title())
        print("Level: "+ str(self.level))
        print("Health: "+ str(self.life))

class Admin(User):
    def __init__(self, f_name, l_name, level, life):

        super().__init__(f_name, l_name, level, life)
        self.privilege = 'I can control users.'
    
    def show_privilege(self):
        print("This admin can"+ self.privilege)


admin321 = Admin('Elroy', 'Sushmita', 30, 40)
admin321.show_privilege()

