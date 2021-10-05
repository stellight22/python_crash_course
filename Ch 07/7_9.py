sandwich_orders = ['pastrami', 'BLT', 'cheese steak', 'pastrami', 'meatball', 'pastrami']
print("The deli has run out of pastrami")

counter = 0
new_sandwich = []
while counter < len(sandwich_orders)-1:
    counter += 1
    if sandwich_orders[counter]== 'pastrami':
        continue
    else:
        new_sandwich.append(sandwich_orders[counter])
print("The available sandwiches are:")
print(new_sandwich)

    