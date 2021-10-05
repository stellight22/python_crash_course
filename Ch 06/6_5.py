#6-5 rivers
"""
make a dictionary containing three major rivers and the country
each river runs through. 
use a loop to print a sentence about each river
use  a loop to print the name of each river in dict
use a loop to print the name of each country in dict
"""

rivers = {
    'missisippi': 'USA',
    'Nile': 'Egypt',
    'Congo': ['Republic of Congo', 'Zaire', 'Angola', 'Zambia', 'Cameroon', 'Tanzania'],
    'Han': 'Korea'
}

for r, c in rivers.items():
    print(f"The {r} river is located in {c}.")

for r in rivers.keys():
    print("River name: "+ r)

for c in rivers.values():
    print("Country name: "+ str(c))


    