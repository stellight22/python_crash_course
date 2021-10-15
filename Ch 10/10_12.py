#combine json load and dump and fileNotfoundError
import json

filename = 'fav_nums.json'

def finding_nemo():
    try:
        with open(filename) as file_obj:
            numburp = json.load(file_obj)
            return numburp
    except FileNotFoundError:
        return None

def make_nemo():
    with open(filename, 'w') as file_obj:
        numburp = input("Enter your number:\n")
        json.dump(numburp, file_obj)
    return numburp

make_nemo()
finding_nemo()
