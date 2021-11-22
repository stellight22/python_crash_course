filename = '/Users/interstellahyeon/Documents/GitHub/python_crash_course/Ch 10/Files/pidigits.txt'
with open(filename) as file_obj:
    listy = file_obj.readlines()

str = ''
for line in listy:
    str += line

print(str)
print(len(str))
