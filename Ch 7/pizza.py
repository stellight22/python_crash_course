#7-4 pizza toppings
#write a loop that prompts the user to enter  aseries of pizza toppings until 
#they enter a quit value
#print adding topping for each input

prompt = "Enter a topping to add"
prompt +=" Enter 'q' to quit at any time: "

toppings = ""

while toppings != 'q':
    toppings = input(prompt)
    if toppings != 'q':
        print(f"Adding {toppings} to the pizza")

