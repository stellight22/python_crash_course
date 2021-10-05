#8-11 great magicians
# def main():
#     magicians = ['magi', 'yoda', 'mickey', 'dumbledore']
#     new_magis = []
#     great = "The Great"
#     show_magicians(magicians)
#     make_great(magicians, great, new_magis)
#     print(magicians)
#     print(new_magis)

# def show_magicians(magicians):
#     for magic in magicians:
#         print(magic.title())

# def make_great(magicians, great, new_magis):
#     for m in magicians:
#         m += great 
#         new_magis.append(m)
    
def main():
    listy = [1,2,3,4,5]
    print(add_to_l(listy[:]))
    print(del_from_l(listy[:]))
    print(show_l(listy[:]))
    print (listy)

def add_to_l(listyy):
    listyy.append(9)
    return listyy

def del_from_l(listyy):
    listyy.remove(3)
    return listyy

def show_l(listyy):
    for val in listyy:
        print("-")
    return listyy

    
if __name__ == "__main__":
    main()
        
        
        

        