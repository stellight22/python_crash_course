



def main(number,  color, booool = True):
    print("number:", number)
    print("color:", color)
    print("bool:", booool)

#default values
main(20, False)

#keyword aruguments
main(color = 'red', number = 44)

#positional arguments
main(30, 'blue', False)