#using range() to make a list of nums

number_list = list(range(1,7))
print(number_list)

even_number_list = list(range(2, 11, 2))
print(even_number_list)

odd_number_list = list(range(1,12, 2))
print(odd_number_list)

#list comprehension
#SUPER important to use []
list_comprehension = [x**2 for x in range(2,10)]
print(list_comprehension)


"""
[1, 2, 3, 4, 5, 6]
[2, 4, 6, 8, 10]
[1, 3, 5, 7, 9, 11]
[4, 9, 16, 25, 36, 49, 64, 81]
"""
