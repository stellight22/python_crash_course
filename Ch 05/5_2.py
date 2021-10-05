#5-2 more conditional tests

strawberry = 'awesome'
blackberry = 'the greatest'
rice = 'yum'
coffee = 'addiction'
gym = 'religion'

print(strawberry == blackberry)
print(rice.lower == coffee.lower())
if coffee.lower() == gym.lower():
    print("whee")
else:
    print('aww')

if 'the' in blackberry:
    print(blackberry +" fruit is ")

if blackberry == strawberry:
    print("not the same")
else:
    blackberry = strawberry
    print(blackberry+strawberry.upper())

