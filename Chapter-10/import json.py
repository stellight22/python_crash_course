import json

filename = 'learning_python.txt'
try:
    with open(filename) as file_obj:
        username = json.load(file_obj)
except FileNotFoundError:
    username = input("What is your user_id?")
    with open(filename, 'w') as file_obj:
        json.dump(username, file_obj)
        print("We will remember you when you come back, " + username+ "!")
else:
    print("Welcome back, " + username + "!")

 