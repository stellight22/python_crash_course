#10-6
print("Press 'q' to quit at any time")

while True:
    number_1 = input("Enter a number: ")
    if number_1 == 'q':
        break
  
    number_2 = input("Enter another number: ")
    try:
        added_num = int(number_1)+ int(number_2)
    except ValueError:
        pass

    else:
        print(added_num)
