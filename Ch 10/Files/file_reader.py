with open('python_crash_course/Ch 10/Files/pidigits.txt') as file_object:
    contents = file_object.read()
    print(contents)

filename = 'python_crash_course/Ch 10/Files/pidigits.txt'
with open(filename) as file_object: 
    for line in file_object:
        print(line.rstrip())

#making a list of lines from a file
with open(filename) as file_object:
    lines = file_object.readlines() 
for line in lines:
    print(line.rstrip())

#making a string from the list object
