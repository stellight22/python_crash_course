#functions and arbitrary arguments
 
def make_pizza(size, *toppings):
    print("\nBaking a "+ str(size)+ "-in pizza with the following toppings:")
    for topping in toppings:
        print("- "+ topping)

