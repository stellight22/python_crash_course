
from typing import Type



try:
    num1 = int(input("Enter a number: \n"))
    num2 = int(input("Enter another number: \n"))
except ValueError:
    print("Enter a number please")
else:
    num3 = int(num1 + num2)
    print(num3)


