#6-7 people
#make a dictionary of two dictionaries for two people

one_plus_one = {
    'Peep_1' :{
        'age': 30,
        'industry': 'design',
        'height': 4,
    },
    'Peep_2' : {
        'age': 40,
        'industry': 'technology',
        'height': 5,
    },
}
for person, personal in one_plus_one.items():
    print(f"The person {person} is {personal['age']} years old, has business in {personal['industry']} and is {personal['height']} levels tall.")

