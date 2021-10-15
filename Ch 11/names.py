from name_function import get_formatted_name

print("Enter 'q' at any time to quit.")
while True:
    first = input("First name: \n")
    if first =='q':
        break
    last = input("Enter last name:\n")
    if last == 'q':
        break

    full_name = get_formatted_name(first, last)
    print(f"The name is {full_name}")