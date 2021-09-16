filename ='learning_python.txt'
with open('learning_python.txt') as file_object:
    lines = file_object.readlines()

lines_output = ''
for line in lines:
    lines_output += line.strip()

print(lines_output[:])

lines_output2 =''
for line in lines:
    lines_output2 += line.rstrip()   # this makes a list
print(lines_output2[:])
