# call a simple function that does not take any args and call the function
def simple():
    print("function simple called")

simple()

#write a function that takes in an argument called stella and prints out stella

def stella(stella):
    print(stella)

stella('stella')

#positional argument

def r123(r1, r2):
    r3 = int(r1/r2)
    return r3

print(r123(9,3))
print(r123(r2 =3,r1 =9))    #keyword argument

#default values
def stove(r2, r4 = 40, r5 = ''):
    print(r2)
    print(r4)
    print(r5)

stove(4)
stove(7, 50)








