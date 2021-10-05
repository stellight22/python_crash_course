#if/else

requested_toppings = {
    'apple': 'fruit',
    'amazon': 'place'
}
print(requested_toppings.items())
print(requested_toppings)

if 'apple' in requested_toppings.keys():
    print("Add anchovies")
else:
    print("hold the anchovies!")

    