#container objects

#in, not in

##sequential##
#lists
#tuples
#strings


##unordered##
#dictionary
#sets

sets = {'a','f','h'}
sets.pop()

print(sets)
#sets.remove('a')
print(sets)

#use list comprehension to print each character in a string

stringg = 'piepiepiepiepie'
listt = [x for x in stringg]
print(listt)

#using break in conditional statement

for x in range(0,7):
    print(x)
    if x == 6:
        break
    else:
        continue
