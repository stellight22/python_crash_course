#6-11 

cities = {
    'Hallstatt': {
        'country': 'Austria',
        'fact': 'oldest village in Europe',
        'population': 850
    },
    'Cesky Krumlov':{
        'country': 'Czech Republic', 
        'fact': 'an S-shaped loop and has castle',
        'population': 12980
    },
    'Stepantsminda': {
        'country': 'Georgia',
        'fact': 'snowy hilltops and hotsprings',
        'population': 1326
    },
    'Furnas':{
        'country': 'The Azores',
        'fact': 'hydropolis of the world, geysers',
        'population': 1439

    },
    'Rothenburg ob der Tauber':{
        'country': 'Germany',
        'fact': 'medieval castles and vineyards',
        'population': 11391
    },
    'Ibaraki' :{
        'country': 'Japan',
        'fact': 'bright coral bushes',
        'population': 2800000
    },
    'Pingvallavatn':{
        'country': 'Iceland',
        'fact': 'submerged rock lake, two continents',
        'population': 0
    },

}

for place, place_facts in cities.items():
    print(f"The wonderous {place}, located in {place_facts['country']} has {place_facts['fact']}!")
    print(f"\tThere are {place_facts['population']} inhabitants as of 2019.")
    if place_facts['population'] > 100000:
        print(f"\tit is a bit crowded.... be safe!")
    else:
        print(f"\tDon't worry, you will have it to yourself.")
