#11-1

def get_data_city(city, country, population = 0):
    city_stats = city.title()+ ", "+ country.title()
    if population:
        city_stats += ", population: "+ str(population)
    return city_stats





