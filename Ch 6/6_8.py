#6-8 Pets

Pets = {
    'dog': {
        'breed': 'poodle',
        'owner': 'Sally',
        'region': 'Portugal',
        'trained(Y/N)': 'N',
    },
    'snake':{
        'color': 'alexandrite',
        'owner': 'Alexandra',
        'region': 'phillippines',
        'trained(Y/N)': 'N',
    },
}

for pet_type, pet_deets in Pets.items():
    print("The details of the following pet type "+ pet_type.upper()+ " are as follows:")
    print("\tThe owner of this pet is: "+ pet_deets['owner']+".")
    print(f"\tThis pet is from {pet_deets['region']} and is it trained? Surprisingly: {pet_deets['trained(Y/N)']}!")