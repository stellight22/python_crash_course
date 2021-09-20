#4-7 make a list of the multiples of 3 from 3 to 30, use a for loop to print
threes = []
for t in range(3,31,3):
    threes.append(t)
print(threes)

#alt method

threes_list = [x for x in range(3,31,3)]
print(threes_list)

"""
[3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
[3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
"""