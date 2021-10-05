#5-9 

usernames = ['admin', 'Sherry', 'Pinot', 'Cabernet', 'dessert']
if usernames:
    for user in usernames:
        if user.lower() == 'admin':
            print("Hello, Admin. You are the first to login.")
        else:
            print(f"Hello, {user.title()} welcome back! Let's get cookin.")
else:
    print("We need some mo userz")

usernames.remove('admin')
usernames.remove('Sherry')
usernames.pop()
del usernames[0]
print(usernames)
usernames.remove('Cabernet')

if usernames:
    for user in usernames:
        if user.lower() == 'admin':
            print("Hello, Admin. You are the first to login.")
        else:
            print(f"Hello, {user.title()} welcome back! Let's get cookin.")
else:
    print("We need some mo userz")

    

