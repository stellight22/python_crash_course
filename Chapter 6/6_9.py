#6-9 favorite places

favorite_places_dict = {
    'Ali': ['Cairo', 'California', 'Croatia'],
    'Suzy': ['Morocco', 'Maui', 'Memphis'],
    'Crypto': ['Internet', 'Bed', 'Home']
}

for name, places in favorite_places_dict.items():
    print(f"Hey there, {name}! How have you been?")
    print(f"{name}: I've been cruising through {places}")