#Ch9-4 exercises

#Exercises 9-4 and 9-5 focus on updating count of customers or login attempts for ex

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(self.restaurant_name.title())
        print(self.cuisine_type.title())

    def open_restaurant(self):
        print("The restaurant "+ self.restaurant_name.title()+ " is open for business!")

    def total_served(self):
        print("The number of people served is: "+ str(self.number_served))

    def set_number_served(self, num):
        num = self.number_served
    
    def increment_number_served(self, nums):
       self.number_served += nums

restaurant = Restaurant("Breakfast at Tiffany's", "French")

restaurant.number_served = 90
restaurant.total_served()

restaurant.increment_number_served(40)
restaurant.total_served()


