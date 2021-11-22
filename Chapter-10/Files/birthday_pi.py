filename = '/Users/interstellahyeon/Documents/GitHub/python_crash_course/Ch 10/Files/pi_million_digits.txt'

with open(filename) as f:
    listt = f.readlines()

stringg = ''
for line in listt:
    stringg += line.strip()

# write a program to write the index of your birthday in pi stringg
birthday = '1022'
#string[index of 1], [index of 0], [index of 2], [index of 2]

for x in range(0,len(stringg)-1):
    if stringg[x] == '0' and stringg[x+1] == '6' and stringg[x+2] == '1' and stringg[x+3] == '0' and stringg[x+4] == '9' and stringg[x+5] == '2':
        print(f"{x} : {stringg[x]}{stringg[x+1]}{stringg[x+2]}{stringg[x+3]}")









