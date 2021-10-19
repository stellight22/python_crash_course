# #function that returns a dictionary

# d2 = {
#     'today': 'study',
#     'tomorrow': 'play', 
#     'habit': 'repeat'
# }
# def return_dict(d2):
#     d2['return'] = 'bridge'
#     return d2

# print(return_dict(d2))

# #function that uses loops and lists
# l = [1,4,8,32,32]
# def looper(l):
#     l2 = [x*3 for x in l]
#     return l2

# print(l)
# print(looper(l))

# x_list = [x*4 for x in looper(l)]

# d = looper(l)
# x_listy = [x*4 for x in d]
# print(x_list)

#a list with set of numbers

f = [1,2,3,5,6,8,9]

#every off number add 2

def odder(f):
    for x in range(1,len(f)):
        if x % 2 == 1:
            f[x] +=2
    return f

print(f)
print(odder(f[:]))
print(f)

x = 3

def add(x):
    x +=1
    return x

print(x)
print(add(x))
print(x)

#to not change the original list, pass the copy of the list as an ARGUMENT, not parameter

#variables have addresses directly to the object, directly using the value
#lists have addresses to the pointers directing to the iterable object which holds addresses