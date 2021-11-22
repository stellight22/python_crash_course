#write a function to create a dictionary, print a dictionary
#write a function to add to a dictionary, then return
# write a function to delete a value from a dictionary then return the dictionary

def main():
    dictionari = {'key2': 3, 'key4': 'C2569'}
    print(add_dict(dictionari))
    print(del_dict(dictionari))
    print(dictionari)


def add_dict(dictionarii):
    for x in range(10,15):
        dictionarii[x] = x +3
    return dictionarii
    
def del_dict(dictionarii):
    for k,v in dictionarii.items():
        if dictionarii[k] < v:
            del dictionarii[k]
    return dictionarii
        

if __name__ == "__main__":
    main()