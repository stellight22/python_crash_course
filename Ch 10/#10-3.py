#10-3
filename = 'learning_python.txt'

with open(filename, 'w')as file_object:
    name_list = input("Welcome, enter your first name: ")
    file_object.write(name_list.title())

with open(filename, 'a')as file_object:
    name_list_2 = input("also, what is your last name?")
    file_object.write(" " +name_list_2.title())



    