print("Enter 'q' to quit")

while True:
    try:
        num1 = input("Enter a number: \n")
        if num1 == 'q':
            break
        num2 = input("Enter another number: \n")
        if num2 =='q':
            break
        else:
            num1 = int(num1)
            num2 = int(num2)
    except ValueError:
        pass
    else:
        num3 = int(num1 + num2)
        print(num3)
