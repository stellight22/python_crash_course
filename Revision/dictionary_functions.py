#dictionary function
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
    