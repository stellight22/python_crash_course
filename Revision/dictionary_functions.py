#dictionary function
def main():
    dictionari = {
        1:3, 
        5:7,
        }
    print(add_dict(dictionari))
    print(del_dict(dictionari))
    print(dictionari)


def add_dict(dictionarii):
    for x in range(10,15):
        dictionarii[x] = x +3
    return dictionarii
    
def del_dict(dictionarii):
    for k in dictionarii:
        if dictionarii[k] < k:
            del dictionarii[k]
    return dictionarii
        

if __name__ == "__main__":
    main()
    