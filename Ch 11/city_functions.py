def city_country(city, country, population = ''):
    str = ''
    if population:
        str = city.title() + ', '+ country.title() + ' population: ' + population
    else:
        str = city.title() + ', ' + country.title()
    return str


print(city_country('cancun', 'mexico'))
print(city_country('cancun', 'mexico', '4000000'))
