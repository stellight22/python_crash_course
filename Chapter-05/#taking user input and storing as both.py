#taking user input and storing as both
#int and string
#from CS 3A by Mike Murphy(copyrights)

"""test whether or not a user-entered integer is even or odd using %"""

# get user's age and store both as string and int
user_str = input("Enter an int: ")
user_int = int (user_str)

if (user_int % 2 == 0):
   print(f"{user_str} is even.")
else:
   print(f"{user_str} is odd.")
   