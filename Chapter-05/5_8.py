#5-8 lists and if statements

usernames = ['admin', 'Sherry', 'Pinot', 'Cabernet', 'dessert']

for user in usernames:
    if user.lower() == 'admin':
        print("Hello, Admin. You are the first to login.")
    else:
        print(f"Hello, {user.title()} welcome back! Let's get cookin.")