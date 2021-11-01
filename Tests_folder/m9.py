#using try/excepy/finally

number = input("Enter a number :\n")

try:
    number = int(number)
except ValueError:   # runs when try fails
    print("Enter an integer only")
else:  #runs after try works and no exception
    print(number*number)
finally:  #runs always at the end
    print('Thank you for your time')