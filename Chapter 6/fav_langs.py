favorite_languages = {

    'Cameron': 'java', 
    'leslie': 'C',
    'Germain': 'ruby',
}

# this prints the key and value as pair of a dict
for name, language in favorite_languages.items():
    print(name.title() + ': ' + language)

another_list = ['paul', 'leslie']
for name in favorite_languages.keys():
    print(name.title())

    if name in another_list:
        print(" Hi " + name.title()+ ", we have you in the dictionary!")
    else:
        print("Hi " + name.title()+ ", we need to get you on file!")

