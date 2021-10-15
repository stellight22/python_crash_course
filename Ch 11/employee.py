class Employee():
    def __init__(self, first_name, last_name, salary,more = 5000):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
    
    def give_raise(self, num):
        self.more = num
        self.salary += num
        
    
joe = Employee('Joe', 'Snyder', 400000)
print(joe.salary)
joe.give_raise(4000)
print(joe.salary)

