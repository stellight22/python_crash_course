#chapter 5 comparative tests
#continuing on if cases

age = 22
ages = 32
icecream = 'butter pecan'
print('butter' in icecream)
print('cherry' in icecream)
perfume = 'my burBerry'
if perfume.lower() == 'my burberry':
    print('that is correct')

if age >=18 and age <=30:
    print('millennial')

if age >=12 or age <= 40:
    print('old enough to know')

if (age <= 30) and (ages >=30):
    print('that is a good age')


given_list = ['gui', 'api', 'stonks']
if 'caramel' not in given_list:
	print('nope')
if 'api' in given_list:
    print('oh yeah')