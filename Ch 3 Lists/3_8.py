#3-8 seeing the world
places_to_go =['provence', 'florence', 'St.Petersberg', 'Alaska', 'London', 'Bora Bora', 'Mumbai']
print("original list:")
print(places_to_go)

print("in abc order, temporary")
print(sorted(places_to_go))

print("in reverse order")
places_to_go.reverse()
print(places_to_go)

print("reverse again")
places_to_go.reverse()
print(places_to_go)

print("reverse abc order")
places_to_go.sort(reverse = True)
print(places_to_go)

print("reverse again")
places_to_go.sort(reverse = False)
print(places_to_go)