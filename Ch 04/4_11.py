#4-11 
favorite_pizzas = ['bianca', 'veggie', 'thin crust']
for type in favorite_pizzas:
    print("I love "+ type + " pizza!")

friend_pizzas = favorite_pizzas[:]
print(friend_pizzas)
favorite_pizzas.append('bbq pineapple')
#checking that friend pizzas is still w/o pineapple
print(favorite_pizzas)

print(friend_pizzas)
friend_pizzas.append('italian sausage')

print("My favorite pizzas are:")
for pizza in favorite_pizzas:   
    print("\t"+pizza+ " pizza")

print("My friend's favorite pizzas are:")
for zza in friend_pizzas:
    print("\t"+zza +" pizza")


