#9-1 class restaurant 
class Restaurant():
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine
    
    def describe_restaurant(self):
        print(self.name+ " serves "+ self.cuisine + " food")
    
    def open_restaurant(self):
        print(self.name+ " is open for business!")

#instantiate restaurant

rocky_icecream = Restaurant("Mel's Diner", "American")

rocky_icecream.describe_restaurant()
rocky_icecream.open_restaurant()
    
    