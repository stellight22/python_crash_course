#checking usernames

current_users = ['a', 'b', 'c', 'd', 'e']
new_users = ['f', 'g', 'h', 'a', 'b']

for user in new_users:
    if user.lower() in current_users:
        print("already taken")
    else:
        print("the name can be used")