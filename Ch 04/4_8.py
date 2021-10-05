#4-8 Cubes
# make a list of the first 10 cubes of integers 1 to 10 and use a for loop to print
cubics =[]
for x in range(1,11):
    cube = x ** 3
    cubics.append(cube)
print(cubics)

cubes = [x**3 for x in range(1,11)]
print(cubes)

"""
[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
"""