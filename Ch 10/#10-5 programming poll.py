#10-5 programming poll
filename = '/Users/interstellahyeon/Documents/GitHub/python_crash_course/Ch 10/learning_python.txt'

print("Enter 'n' when done")

while True:
    answer = input("Why do you code?")
    if answer == 'n':
        break
    else:
        with open(filename, 'a')as file_object:
            file_object.write(answer+"\n")