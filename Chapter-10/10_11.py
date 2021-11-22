import json

filename = 'fav_nums.json'

with open(filename, 'w') as file_obj:
    name = input("Enter name: \n")
    json.dump(name, file_obj)

with open(filename) as file_obj:
    name = json.load(file_obj)
    print("Hello, "+ name +"!")
    