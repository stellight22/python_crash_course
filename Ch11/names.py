from name_function import get_formatted_name

print("Enter 'q' at any time to quit.")
while True:
    first = input("\nEnter employee first name: ")
    if first == 'q':
        break
    last = input("\nEnter employee last name:")
    if last =='q':
        break

    formatted_name = get_formatted_name(first, last)
    print("\tThe employee name is: "+ formatted_name )
    