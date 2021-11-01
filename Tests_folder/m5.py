#unpacking a list

complex = [1,2,3,(4,5), 'rain']
*a, b, t, s  = complex
print(*a)
print(b)
print(t)
print(s)

#unpack a tuple
tup = ('t', 'u', 'p','p','e','r','w','a','r','e')
g, o, *t = tup
print(g)
print(o)
print(*t)

#unpack a dictionary
dicty = {
    'key 1': 'movienight', 
    'key 2': 'study', 
    'key 3': 'nap',
}

x, y,z = dicty
print(f"{x} : {dicty[x]}")
print(f"{y} : {dicty[y]}")
print(f"{z}: {dicty[z]}")

#create a set
setty = {'t', 'u', 'p','p','e','r','w','a','r','e'}
one, two, three, four, five, six, sev = setty
print(one)
print(two)
print(three)
print(four)
print(five)
print(six)
print(sev)

#when you unpack sets and dictionaries, the order will change
#only the order of list and tuple items are preserved because lists are ordered

