#using arbitrary keyword arguments

def build_profile(first, last, **user_stats):
    profile = {}
    profile['first_name ']= first
    profile['last_name'] = last
    for key, value in user_stats.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert', 'einstein', location = 'london', field = 'physics')
print(user_profile)

# 8-14. Cars: Write a function that stores information about a car in a diction- ary . 
# The function should always receive a manufacturer and a model name . 
# It should then accept an arbitrary number of keyword arguments . Call the func- tion with the required information and two other name-value pairs,
#  such as a color or an optional feature . Your function should work for a call like this one:
 #car = make_car('subaru', 'outback', color='blue', tow_package=True)

def build_car(make, model, **car_stats):
    deets = {}
    deets['brand'] = make
    deets['series'] = model
    for key, value in car_stats.items():
        deets[key] = value
    return deets

dream_car = build_car('McLaren', '765LT', color = 'red', style = 'coupe')
print(dream_car)