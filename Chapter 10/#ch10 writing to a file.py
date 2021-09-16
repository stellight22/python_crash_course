#ch10 writing to a file

filename = 'learning_python.txt'

with open(filename, 'w') as file_object:
    file_object.write("bleh bleh bleh\n")
    file_object.write("this is the second line of bleh\n")

#appending
with open(filename, 'a') as file_object:
    file_object.write("I'm also going to add to end of file\n")
    file_object.write("more bleh bleh bleh\n")

