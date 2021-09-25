#8-14 cars
def build_car(make, year, **add_features):
    car = {}
    car['make'] = make
    car['year'] = year
    for key, value in add_features.items():
        car[key] = value
    return car

my_car = build_car('mustang', 2020, color = 'red', option = 'full' )
print(my_car)
