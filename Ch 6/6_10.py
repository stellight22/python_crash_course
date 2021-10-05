#6-10 

person_and_num = {
    'person1': [22, 45,60],
    'person2': [44, 33, 12],
    'person3': [17, 60, 9],
}

for person, num in person_and_num.items():
    print(f"Person: {person} has the favorite numbers: {num}.")

for person, num in person_and_num.items():
    print("The person, "+ person.title()+" has the following favorite numbers:")
    for n in num:
        print("\t", n)