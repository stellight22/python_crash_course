#Ch 11-3
class Employee():
    def __init__(self, f_name, l_name, salary):
        self.f_name = f_name
        self.l_name = l_name
        self.salary = salary

    def give_raise(self, addition = 5000):
        self.salary += addition

    
    
