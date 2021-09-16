#chapter 7 input and while loops

name = input("Enter your name:")
print("hello, " +name)

age = input("Enter your age: ")
age = int(age)
# if you don't convert it to int, it will just be string
#after typecast, you can do:
if age == 18:
    print("you can finally vote!")
elif age < 18:
    print("Aww, so cute!")
else:
    print("You have aged like fine wine;)")

#7-3 ask the user for a number and return if it's a multiple of 10 or not
number = input("enter a number: ")
number = int(number)
if number % 10 ==0:
    print("The number you entered, " + str(number) + ", is a multiple of 10")
else:
    print("The number you entered, " + str(number)+ ", is not divisible by 10")

#while loops and inputs
# to have a program ask over and over again

prompt = "\n Tell me something, and I will echo: "
prompt += "\n Enter 'quit' to exit."
on = True
while on:
    message = input(prompt)

    if message == 'quit':
        on = False
    else:
        print(message)

#continue and loops
# prints only odd numbers in the range
current_num = 0
while current_num <10:
    current_num += 1
    if current_num %2 ==0:
        continue
    print(current_num)

#prints only even numbers from 1-10
even_num = 0
while even_num <10:
    even_num +=1
    if even_num % 2 == 1:
        continue
    print(even_num)


# 7-5. Movie Tickets: A movie theater charges different ticket prices 
# depending on a person’s age . If a person is under the age of 3, 
# the ticket is free; if they are between 3 and 12, the ticket is $10; 
# and if they are over age 12, the ticket is $15 . 
# Write a loop in which you ask users their age, 
# and then tell them the cost of their movie ticket .

question = "Welcome to AMC. Enter the person's age for ticket prices. Enter -1 to exit."
movie_age = input(question)
movie_age = int(movie_age)
if movie_age > -1:
    if movie_age < 3:
        print("The ticket is free")
    elif movie_age <= 12:
        print("The price is 10$")
    elif movie_age >12:
        print("The price is 15$")
else:
    print("invalid age!")

#filling a dictionary with user input

dictionary_of_inputs = {}
question_prompts = True

while question_prompts:
    name = input("Enter first and last name: ")
    answer = input("What is your favorite weekend trip? ")

    dictionary_of_inputs[name] = answer

    another_round = input("Anyone else want to take the survey for prizes?(Y/N? ")
    if another_round == 'N':
        question_prompts = False

print("\n -- Survey Results ---")
for name, answer in dictionary_of_inputs.items():
    print(name + " on the weekends does " + answer + ".")

#7-8. Deli: Make a list called sandwich_orders and fill it with 
# the names of various sandwiches . Then make an empty list called 
# finished_sandwiches . Loop through the list of sandwich orders and 
# print a message for each order, such as I made your tuna sandwich. 
# As each sandwich is made, move it to the list of finished sandwiches . 
# After all the sandwiches have been made,
#  print a message listing each sandwich that was made .

#7-9. No Pastrami: Using the list sandwich_orders from Exercise 7-8,
#  make sure the sandwich 'pastrami' appears in the list at least three 
# times . Add code near the beginning of your program to print a message 
# saying the deli has run out of pastrami, and then use a while loop to 
# remove all occurrences of 'pastrami' from sandwich_orders . 
# Make sure no pastrami sandwiches end up in finished_sandwiches .

finished_sandwiches = []
sandwich_orders = ['sausage', 'everything', 'classic', 'Italian', 'giant', 'veggie', 'po boy', 'pastrami', 'pastrami', 'pastrami']
print("We are sorry, but currently we have run out of pastrami!")
for sandwich in sandwich_orders:
    if sandwich != 'pastrami':
        print("The following sandwich has been completed: " + sandwich + ". Please come to counter.")
        finished_sandwiches.append(sandwich)
    else:
        print("Sorry! No more pastrami today.")

