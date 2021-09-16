#11-1


def city_country(city, country):
    place_dictionary = {'city': city, 'country': country}
    return place_dictionary

city_input = input("Enter the city name:")
country_input = input("And in which country is this city you entered? If you wish to quit, enter 'q' ")
city_country_info = city_country(city_input, country_input)
print("Your next vacation spot is:")
print(city_country_info)




