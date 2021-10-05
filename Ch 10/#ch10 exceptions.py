#ch10 exceptions
#starting with simple division problem

print("Enter two numbers and I will divide them.")
print("Enter 'q' to quit")

while True:
    first_number = input("Enter the number you want to divide:")
    if first_number == 'q':
        break

    second_number = input('Enter the number you want to divide the first number by:')
    try:
        answer = int(first_number)/int(second_number)
    except ZeroDivisionError:
        print("That makes the number undefined")
    else:
        print(answer)

def count_words_in_a_file(filename):
    try:
        with open(filename)as file_obj:
            contents = file_obj.read()
    except FileNotFoundError:
        error_msg = "Sorry, the file " + filename + " does not exist in this computer."
        print(error_msg)
#the file is found
    else:
        words = contents.split()
        num_words = len(words)
        print("The file "+ filename+ " has about " + str(num_words)+ " words.")

filename = 'alice_in_wonderland.txt'
count_words_in_a_file(filename)
filenames = ['alice.txt', 'learning_python.txt', 'peter pancakes.txt']
for file in filenames:
    count_words_in_a_file(file)