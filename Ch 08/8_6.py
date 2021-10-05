#Chapter 8 city names

"""
write a function that takes in the name of a city and its country
the function should return a string formatted:
"Santiago, Chile"
"""
def city_country(city, country):
    full_name = city +", "+ country
    print(full_name.title())

city_country('mexico city', 'mexico')
city_country('la paz', 'bolivia')
city_country('san franciso', 'united states')
