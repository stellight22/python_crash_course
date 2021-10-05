#using arbitrary keyword arguments
#build dictionary from scratch

def build_profile(username, bio, location, **characteristics):
    profile_dict = {}
    profile_dict['id'] = username
    profile_dict['height'] = bio
    profile_dict['city'] = location
    da_keys_2life = profile_dict.keys()
    
    for key, value in characteristics.items():
        profile_dict[key] = value
    return profile_dict


    

user33 = build_profile('user33a!', 174, 'San Francisco', type = 'tiger', interest = 'snakes')
print(user33)

#different ways to print out dictionary
