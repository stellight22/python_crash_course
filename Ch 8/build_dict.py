#dictionary function

def build_hero(f_name, l_name):
    hero = {'first': f_name, 'last': l_name}
    return hero

marvel = build_hero('captain', 'america')
print(marvel)

#adding optional feature

def build_hero(f_name, l_name, cape_color = ''):
    hero = {'first': f_name, 'last': l_name}
    if cape_color:
        hero['cape'] = cape_color
    return hero

baddie = build_hero('black', 'widow')
print(baddie)

captain = build_hero('captain', 'america', 'blue')
print(captain)


