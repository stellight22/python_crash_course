#5-10 Checking usernames

current_users = ['wine-lover', 'dog-lover', 'college kid', 'husband', 'nomad']
new_users = ['wine-lover', 'dogMom', 'goRats', 'pinetree', 'college kid']

for user in new_users:
    if user.lower() in current_users:
        print(f"Dear {user}, that name is taken!")
    else:
        print(f"you may use the username: {user}")
        