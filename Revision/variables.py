#create a variable, list, tuple, dictionary and set

#x is variable
for x in range(1,3):
    print(x)
print(type(x))

y = 4
print(type(y)) 

lista = [1,2,3,4,4,5,5,7]
print(type(lista))

tuple_a = (3,4,7,9, 'c')
print(type(tuple_a))

dictionari_o = {'key_a' : 'a', 'key_b': 'b'}
print(type(dictionari_o))

set_a = {1,2,3,4}
print(type(set_a))
#or
set_b = set(lista)
print(set_b)
