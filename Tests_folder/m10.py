#write to a file then read from a file

filename = '/Users/interstellahyeon/Documents/GitHub/python_crash_course/Tests_folder/hello.txt'

with open(filename,'w') as f:
    f.write('google')

with open(filename) as f:
    r = f.read()
    print(r)