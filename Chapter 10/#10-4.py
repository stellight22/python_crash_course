#10-4

filename = 'learning_python.txt'

greeting = "Hello, guest. Please enter your full name without spaces, press q to quit at any time."

while True:
    guest_names = input(greeting)
    if guest_names == 'q':
        break
    
