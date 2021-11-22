#loop and name function

"""
#infinite times
def get_formatted_name(f_name, l_name):
    full_name = f_name + " " + l_name
    return full_name.title()

while True:
    print("\nEnter your name in the following order:")
    f_name = input("first name: ")
    l_name = input("last name: ")

    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, "+ formatted_name + "!")
"""


#with quit option

def get_formatted_name(f_name, l_name):
    full_name = f_name + ' '+ l_name
    return full_name.title()

while True:
    print("\n Please enter your name: ")
    print("enter 'q' to quit at any time.")

    f_name = input("First name: ")
    if f_name == 'q':
        break

    l_name = input("Last name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, "+ formatted_name + "!")

