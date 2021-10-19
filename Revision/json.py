import json

#the data we are working with
numbers = [1,2,3,4,5,6]

#format for json.dump
filename = 'json_file.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)

#json.load()

with open(filename) as f_obj:
    numbers = json.load(f_obj)

print(numbers)

#json_file was made in the entire module
#the cd must be the file you want the json file to be in 