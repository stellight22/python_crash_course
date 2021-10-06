#9-1 class restaurant 
class Restaurant():
    
    def __init__(self, name, cuisine):
        print("__init__")
        self.name = name
        self.cuisine = cuisine
        self.age += 1
        self.describe_restaurant()
    age = 9
    def describe_restaurant(self):
        print("describe_restaurant")
        # self.name += 1
        self.age += 1
    
    def open_restaurant(self):
        print("open_restaurant")
        # self.cuisine += 1
    
    def close_restaurant():
        print("close restaurant")

    print("close restaurant")

#instantiate restaurant

rock = Restaurant(2,22)
rock.describe_restaurant()
rock.open_restaurant()
print(rock.name)
print(rock.cuisine)
print("age")
print(rock.age)

rock2 = Restaurant(6, 10)
rock2.describe_restaurant()
rock2.open_restaurant()
print(rock2.name)
print(rock2.cuisine)
print("age")
print(rock2.age)

    
