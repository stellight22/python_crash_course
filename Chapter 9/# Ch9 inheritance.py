# Ch9 inheritance
#continuation of class car
class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        print(self.make)
        print(self.model)
        print(self.year)
        print(self.odometer_reading)

    def read_odometer(self):
        print("This car has "+ str(self.odometer_reading)+ " miles on it.")
        
class Battery():

    def __init__(self, battery_size = 70):
        self.battery_size = battery_size
    
    def describe_battery(self):
        print("This car has a "+ str(self.battery_size)+ "kWh battery.")
    
    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        output = "This car can go approx. " + str(range)
        output += " miles on a full charge."
        print(output)

    def upgrade_battery(self):
        if self.battery_size != 85:
            self.battery_size = 85

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 70
    
        #from class Battery
        super().__init__(make, model, year)
        self.battery = Battery()

    #child class can have its own unique functions
    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "kWh battery.")
    
    def fill_gas_tank():
        print("This car doesn't need a gas tank!")

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.describe_battery()

my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()


