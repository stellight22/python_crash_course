#9-5
class User():
    def __init__(self, f_name, l_name, level, life):
        self.f_name = f_name
        self.l_name = l_name
        self.level = level
        self.life = life
        self.login_attempts = 0

#write a method taht increments login attempts by 1
    def increment_login_attempts(self):
        self.login_attempts +=1

    def reset_login_attempts(self):
        self.login_attempts = 0

    def describe_user(self):
        print("Full name: "+ self.f_name.title()+ " "+ self.l_name.title())
        print("Level: "+ str(self.level))
        print("Health: "+ str(self.life))
        print("Login attempts:"+ str(self.login_attempts))

u4547 = User('Jeremy', 'Paupernickel', 45,60)
u4547.describe_user()
u4547.increment_login_attempts()
u4547.increment_login_attempts()
u4547.increment_login_attempts()
u4547.describe_user()

u4547.reset_login_attempts()
u4547.describe_user()

