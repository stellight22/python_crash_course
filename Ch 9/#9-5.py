#9-5
#9-5. Login Attempts: Add an attribute called login_attempts to your User class from Exercise 9-3 (page 166) .
#  Write a method called increment_ login_attempts() that increments the value of login_attempts by 1 . 
# Write another method called reset_login_attempts() that resets the value of login_ attempts to 0 .
# Make an instance of the User class and call increment_login_attempts() several times . Print the value of login_attempts to make sure 
# it was incremented properly, and then call reset_login_attempts() . Print login_attempts again to make sure it was reset to 0 .


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

user_1 = User('Ronnie', 'Barbell')
user_1.describe_user
user_1.login_attempts = 40
user_1.show_logins()
user_1.increment_login_attempts(30)
user_1.show_logins()
user_1.reset_login_attempts()
user_1.show_logins()

