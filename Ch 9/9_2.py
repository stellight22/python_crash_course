#9-2 
class Restaurant():
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine
    
    def describe_restaurant(self):
        print(self.name+ " serves "+ self.cuisine + " food")
    
    def open_restaurant(self):
        print(self.name+ " is open for business!")

R1 = Restaurant("Mel's Diner", "American")
R2 = Restaurant("The Greatest", 'Korean')
R3 = Restaurant("Tia's", "Mexican")

R1.describe_restaurant()
R1.open_restaurant()
R2.describe_restaurant()
R2.open_restaurant()
R3.describe_restaurant()
R3.open_restaurant()