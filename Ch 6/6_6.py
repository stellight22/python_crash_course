#6-6 polling

favorite_lang = {
    'Ashley': 'C',
    'Pam': 'React',
    'Logan': 'Java',
    'Mosley': 'PHP',
    'Kilala': 'HTML',
}
names = ['Pam', 'Logan', 'Kilala', 'Marley', 'Justin']

for name in favorite_lang.keys():
    if name in names:
        print("The person is in the dictionary")
    else:
        print("On their own")
        

