#7-3 Ask the user for a number, and report whether it's a multiple of 10

test_for_ten = input("Enter a number:")
if int(test_for_ten) % 10 == 0:
    print("The number is a multiple of ten")
else:
    print("This number is not divisible by 10")