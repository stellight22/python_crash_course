# 6-8
"""
 6-8. Pets: Make several dictionaries, where the name of each dictionary is the name of a pet . 
 In each dictionary, include the kind of animal and the owner’s name . Store these dictionaries in a list called pets .
  Next, loop through your list and as you do print everything you know about each pet .

6-9. Favorite Places: Make a dictionary called favorite_places . 
Think of three names to use as keys in the dictionary, and store one to three favorite places for each person . 
To make this exercise a bit more interesting, ask some friends to name a few of their favorite places . 
Loop through the dictionary, and print each person’s name and their favorite places .

6-11. Cities: Make a dictionary called cities . Use the names of three cities as keys in your dictionary . 
Create a dictionary of information about each city and include the country that the city is in, its approximate population, 
and one fact about that city . The keys for each city’s dictionary should be something like country, population, and fact . 
Print the name of each city and all of the infor- mation you have stored about it .

"""
Pets ={
'Gunther' : {
    'type': 'schnauzer',
    'owner': 'Cecile',
},
'Solomon' : {
    'type': 'Aussie',
    'owner': 'Jordana',
}
}
for pet in Pets.items():
    print("Here are the following details to each pet:")
    print(pet)


favorite_places = {
    'Ernie': ['birdwatching', 'Death Valley', 'Morro Bay'], 
    'Stella': ['Brooklyn Bridge', 'Hawaii', 'SF fitness'], 
    'Ratatouille': ['Manchego', 'gouda', 'provolone'],
}
for name, favorites_list in favorite_places.items():
    print("\n" + name.title() +" has the following favorites:")
    for places in favorites_list:
        print("\t" + places.title())

Cities ={
    'Tokyo': {
        'country': 'Japan', 
        'fun fact': 'make hentai'

    },
    'Atlanta': {
        'country': 'The South', 
        'fun fact': 'K town'
    },
    'Los Angeles': {
        'country': 'West Coast',
        'fun fact': 'stop breast reduction'
    },
}
for city, city_info in Cities.items():
    location = city_info['country']
    one_liner = city_info['fun fact']
    print("\nCity: "+ city+ " is in "+ location.title()+ " and the Joe Schmoe episode is titled: Joe goes to " + one_liner.title())