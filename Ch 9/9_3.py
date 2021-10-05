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


user1 = User('Gerome', 'Bundt', 23, 70)
user1.describe_user()