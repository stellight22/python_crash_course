#chapter 9
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

    def update_odometer(self, mi):
        self.odometer_reading = mi
    
    #this function is for additional logic step so that the update of the odometer
    #only happens for increase, not decrease since car mileage only goes up
    def modify_update_mileage(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("you can't roll back an odometer")

    #or we can increment using a method
    def increment_odometer(self, mo_miles):
        self.odometer_reading += mo_miles

my_new_car = Car('audi', 'a4', '2020')
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

#mod attr thru method
    

my_new_car.update_odometer(45)
my_new_car.read_odometer() 

my_used_car = Car('McLaren', '765LT', 2019)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(25000)
my_used_car.read_odometer()

my_used_car.increment_odometer(4000)
my_used_car.read_odometer()


#



