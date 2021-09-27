#Ch 9 accessing multiple classes
#instances as attributes

class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.miles = 0

    def get_descriptive_name(self):
        desc = str(self.year)+ " " + self.make + ' '+ self.model
        return desc.title()

    def read_odometer(self):
        print("This car has"+ str(self.miles) + " miles on it.")

    def update_odometer(self, more_miles):
        if more_miles >= self.miles:
            self.more_miles = self.miles
        else:
            print("You can't decrease miles on a car!")

    def increment_odometer(self, m):
        self.miles += m
# another class related to cars

class Grade():
    def __init__(self, grade = 400):
        self.grade = grade
    
    #like a getter
    def describe_grade(self):
        print("This car model grade is :" + str(self.grade))



#child class
class HybridCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.level = Grade() #using another class instance as attribute
        self.finish = 'different'
    
    def describe_finish(self):
        print("This hybrid has a finish that makes it " + self.finish + " from the parent models.")

mcLarenz756 = HybridCar('mcLaren', 'turbo', 2030)
mcLarenz756.level.describe_grade()

