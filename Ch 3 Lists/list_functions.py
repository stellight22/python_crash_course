#Introducing Lists

friends = ['bo', 'mo', 'sol', 'ra', 'cam', 'rob']
for friend in friends:
    print(friend)

friends.append('bro')

friends.insert(0, 'newbie')

del friends[3]

friends.pop()
friends.remove('ra')

print(friends)