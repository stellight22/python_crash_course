#nested dictionary

outer = {
    'inner1' :{
        'key1': 'value1',
        'key2': 'value2',
    },
    'inner2' :{
        'key1': 'apple',
        'key2': 'banana',

    },
}
print(outer)
for key, value in outer.items():
    print(key, end = " ")
    for k,v in value.items():
        print(f"{k} : {v}",end = " ")
    print()    
    
    