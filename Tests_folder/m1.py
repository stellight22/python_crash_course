dicty = {
    'key 1': 'movienight', 
    'key 2': 'study', 
    'key 3': 'nap',
}

print(dicty.values())
print(dicty['key 1'])
print(dicty['key 2'])
print(dicty['key 3'])

dicty['key 4'] = 'little dicty'
print(dicty)

lengthy = len(dicty)
 
d_list = [x for x in dicty]
print(d_list)

for d in d_list:
    print(f"key is {d} and value is {dicty[d]}")