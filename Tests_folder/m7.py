#example of or and and in a program

number = 60

if number == 60 and number > 40:
    print("whoo")

if number == 50 or number < 100:
    print("whee")


double_list = [['k','i'],3,4 ]
if ['k','i'] in double_list:
    print("yes, you can check if a list has a list")

#string methods

string_cheese = 'goat milk'

#recursive function

def summation(n):
    if n == 0:
        return 0
    else:
        return n + summation(n-1)

print(summation(5))

print(ord('r'))
print(chr(38))