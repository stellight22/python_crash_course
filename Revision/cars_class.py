#this one is on superclasses
#children class

class Car():
    def __init__(self, *make):
        self.make = make
        self.miles = 0

    def get_descriptive_name(self):
        print(self.make)
        print("describe car")

    def read_odometer(self):
        print("This car has"+ str(self.miles) + " miles on it.")

    def update_odometer(self, more_miles):
        if more_miles >= self.miles:
            self.more_miles = self.miles
        else:
            print("You can't decrease miles on a car!")

    def increment_odometer(self, m):
        self.miles += m

#child class
class HybridCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.finish = 'different'
    
    def describe_finish(self):
        print("This hybrid has a finish that makes it " + self.finish + " from the parent models.")


mclaren223 = HybridCar(year = 4400,make ='mcLaren', model ='LT745')

print(mclaren223.get_descriptive_name())
mclaren223.describe_finish()