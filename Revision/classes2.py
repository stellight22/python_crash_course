#9-2 
class Restaurant():
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine
        self.length = 60
    
    def describe_restaurant(self):
        print(self.name+ " serves "+ self.cuisine + " food")
        self.open = 'yes'
    
    closed = 90
    
    def open_restaurant(self):
        print(self.name+ " is open for business!")




print(Restaurant.closed)

Restaurant.closed = 100

print(Restaurant.closed)
print(Restaurant.closed)

R1 = Restaurant("Mel's Diner", "American")
R2 = Restaurant("The Greatest", 'Korean')
R3 = Restaurant("Tia's", "Mexican")
print(R1.closed, R2.closed)
R1.length = 70
R1.closed = 80
R2.closed = 77
R1.describe_restaurant()
R1.open_restaurant()
R2.describe_restaurant()
R2.open_restaurant()
R3.describe_restaurant()
R3.open_restaurant()
print(R1.closed, R2.closed)
Restaurant.closed = 66
print(R1.closed, R2.closed)
R4 = Restaurant(888, 'Jamba')
print(R4.closed)
R4.closed = 00
print(Restaurant.closed)
Restaurant.closed = 12
print(R4.closed)

#Restaurant.open_restaurant()