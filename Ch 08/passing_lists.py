#pass a list to a function

def greet_users(names):
    for name in names:
        message = "Hello," + name.title() + "!"
        print(message)

usernames = ['Riley', 'Atkins', 'Blake', 'Sushmita']
greet_users(usernames)

