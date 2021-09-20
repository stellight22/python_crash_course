#4-13 tuples

five_foods = ('italian', 'mexican', 'indian', 'korean', 'Japanese')

#five_foods[3] = 'Chinese'
"""
tuples are set and cannot be modified (in parts)unless the tuple variable is changed entirely through new assignment
"""

five_foods = ('Italian', 'French', 'Indian', 'Korean', 'Russian')
for food in five_foods:
    print("The options for tonight include "+ food + " cuisine.")
"""
original error:
TypeError: 'tuple' object does not support item assignment

The options for tonight include Italian cuisine.
The options for tonight include French cuisine.
The options for tonight include Indian cuisine.
The options for tonight include Korean cuisine.
The options for tonight include Russian cuisine.

"""