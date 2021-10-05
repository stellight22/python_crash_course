#9-6
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(self.restaurant_name.title())
        print(self.cuisine_type.title())

    def open_restaurant(self):
        print("The restaurant "+ self.restaurant_name.title()+ " is open for business!")

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []
    
    def show_flavors(self):
        print(self.flavors)

Carol_Baskin_Robins = IceCreamStand('Baskin', 'dessert')
Carol_Baskin_Robins.flavors = ['matcha', 'coconut', 'butter pecan']

Carol_Baskin_Robins.show_flavors()
