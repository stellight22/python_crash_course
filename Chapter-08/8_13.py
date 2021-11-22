#8-13 user4 profile

def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key]= value
    return profile

user_profile = build_profile('kimmy', 'kardashie', location = 'los angeles', industry = 'entertainment')

print(user_profile)