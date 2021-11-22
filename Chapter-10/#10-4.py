#10-4
"""
Guest Book: Write a while loop that prompts users for their name . 
When they enter their name, print a greeting to the screen and add a line 
recording their visit in a file called guest_book.txt . 
Make sure each entry appears on a new line in the file .
"""

filename = '/Users/interstellahyeon/Documents/GitHub/python_crash_course/Ch 10/guest_book.txt'

greeting = "Hello, guest. Please enter your full name without spaces, press q to quit at any time."

while True:
    guest_names = input(greeting)
    if guest_names == 'q':
        break
    else:
        with open(filename, 'a') as file_obj:
            file_obj.write(f"{guest_names}\n")
    
