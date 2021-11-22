#9-4 
class Restaurant():
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine
        self.number_served = 0
    
    def describe_restaurant(self):
        print(self.name+ " serves "+ self.cuisine + " food and "+ str(self.number_served) +" people per day.")
    
    def open_restaurant(self):
        print(self.name+ " is open for business!")
    
    def set_number_served(self, num_ser):
        self.number_served = num_ser
    
    def increment_number_served(self, nums):
        self.number_served += nums

r1 = Restaurant("Mel's Diner", "American")

r1.describe_restaurant()
r1.open_restaurant()

r3 = Restaurant("Tiffany's Creme Brulee", "Patisserie" )
r3.set_number_served(89)
r3.increment_number_served(60)
r3.describe_restaurant()


