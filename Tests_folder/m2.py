#embed a dictionary within in dictionary

master_dict = {

    'inner_1' : {
        'kk1': 'vv1',
        'kk2': 'vv2',

    },
    'inner_2' : {
        'kk3': 'vvv1',
        'kk4': 'vvv2',

    },

}

#with .items()
for inner_name, contents in master_dict.items():
    for k, v in contents.items():
        print(f"The inner key is {k} and the inner value is {v}")

#without .items():
inner_names = [k for k in master_dict]
#print(inner_names)
for q in inner_names:
    print(q)
    print(master_dict[q])

for r in master_dict[q]:
    print(r)
    print(master_dict[q][r])


for x in master_dict:
    for y in master_dict[x]:
        print(f"key{y} and value {master_dict[x][y]}")
