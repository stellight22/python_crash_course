#7-6 Three exits:
"""
Write a program that will
    -use  a conditional test in the while statement to stop the loop
    - use an active variable to control how long the loop runs
    - use a break statement to exit the loop when the user enters a 'quit' value

"""
#1. using conditional case
prompt = "Enter a number"
prompt += "Enter '0' to quit."
information = ""
total = 0

while information != '0':
    information = input(prompt)
    total += int(information)

    if information != '0':
        print(information)
print("\tThe sum of all numbers is: " + str(total))

#2. Use a counter to run fixed number of times
counter = 0
while counter <10:
    counter += 1
    if counter == 1:
        print(str(counter) +": one")
    elif counter == 2:
        print(str(counter) +": two")
    elif counter == 3:
        print(str(counter) +": three")
    elif counter == 4:
        print(str(counter) +": four")
    elif counter == 5:
        print(str(counter) +": five")
    elif counter == 6:
        print(str(counter) +": six")
    elif counter ==7:
        print(str(counter) +": seven")
    elif counter ==8:
        print(str(counter) +": eight")
    elif counter ==9:
        print(str(counter) +": nine")
    else:
        print(str(counter) +": ten")

#3. Use quit variable

