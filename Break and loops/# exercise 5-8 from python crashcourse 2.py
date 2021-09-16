# exercise 5-8 from python crashcourse 2nd edition
from typing import List
"""
5-8. Hello Admin: Make a list of five or more usernames, including the name
'admin'. Imagine you are writing code that will print a greeting to each user
after they log in to a website. Loop through the list, and print a greeting to
each user:
•	 If the username is 'admin', print a special greeting, such as Hello admin,
would you like to see a status report?
•	 Otherwise, print a generic greeting, such as Hello Eric, thank you for logging in again.
5-9. No Users: Add an if test to hello_admin.py to make sure the list of users is
not empty.
•	 If the list is empty, print the message We need to find some users!
•	 Remove all of the usernames from your list, and make sure the correct
message is printed.
5-10. Checking Usernames: Do the following to create a program that simulates
how websites ensure that everyone has a unique username.
•	 Make a list of five or more usernames called current_users.
•	 Make another list of five usernames called new_users. Make sure one or
two of the new usernames are also in the current_users list.
•	 Loop through the new_users list to see if each new username has already
been used. If it has, print a message that the person will need to enter a
new username. If a username has not been used, print a message saying
that the username is available.
•	 Make sure your comparison is case insensitive. If 'John' has been used,
'JOHN' should not be accepted.
5-11. Ordinal Numbers: Ordinal numbers indicate their position in a list, such
as 1st or 2nd. Most ordinal numbers end in th, except 1, 2, and 3.
•	 Store the numbers 1 through 9 in a list.
•	 Loop through the list.
•	 Use an if-elif-else chain inside the loop to print the proper ordinal ending for each number. Your output should read "1st 2nd 3rd 4th 5th 6th
7th 8th 9th", and each result should be on a separate line.
"""

users =['admin', 'kelsy', 'tushar', 'adonis', 'kimmy']
for user in users:
    if user =='admin':
        print ("Hello admin. Would you like to see a status report?")
    else:
        print("Hello, " + user.title()+ ". Welcome to the dark web!")

#5-9 
empty = []
if users == empty:
    print("We need to find more users!")
    users.remove()
    print(users)

#5-10

current_users = ['Abel', 'Cain', 'Drake', 'Boots', 'Nigiri']
new_users = ['Cardi', 'Jay_Z', 'Milo', 'Drake', 'Boots']

for newbie in new_users:
    if newbie not in current_users:
        print(newbie + ": "+ "Yay! You are creative and this ID is not already taken!") 
    elif newbie in current_users:
        print(newbie + ": " +"Uh oh! The ID you have created is unoriginal")

#5-11
numbers = [x for x in range(0,10)]
for x in numbers:
    if x == 1:
        print ("1st")
    elif x == 2:
        print("2nd")
    elif x == 3:
        print("3rd")
    elif x == 4:
        print("4th")
    elif x == 5:
        print("5th")
    elif x == 6:
        print("6th")
    elif x == 7:
        print("7th")
    elif x == 8:
        print("8th")
    else:
        print("9th")
