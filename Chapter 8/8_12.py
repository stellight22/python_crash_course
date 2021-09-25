#arbitrary number of arguments

def sandwiches(bread, *toppings):
    print("The sandwich has the following features:")
    print("bread:", bread)
    for topping in toppings:
        print("-", topping)

sandwiches('whole', 'pepperoni','lettuce')
sandwiches('white', 'ham')
sandwiches('wheat', 'meatballs', 'provolone', 'spinach')

