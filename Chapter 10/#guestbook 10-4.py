#guestbook 10-4

filename = "learning_python.txt"

print("Enter 'q' when you are done")

while True:
    guest = input("Enter name:")
    if guest == 'q':
        break
    else:
        with open(filename, 'w') as file_object:
            file_object.write(guest.title() + "\n")
        print("Hello, " + guest + ", you are on the waitlist!")