#collection of multiple values for key
chef_roll = {
    'rice' : 'white', 
    'protein': ['salmon', 'shrimp'],
    'filling': ['asparagus', 'nori'],
}
print("The chef's roll has " + chef_roll['rice']+ "rice and contains" )
for p in chef_roll['protein']:
    print("\t" + p)
for f in chef_roll['filling']:
    print("\t" + f)

print("for vegan options, try our veggie roll, which contains:")
veg_roll = {
    'rice': 'brown', 
    'protein': 'edamame',
    'extras': 'sweet potato tempura'
}
for value in veg_roll.values():
    print("\t" + value)