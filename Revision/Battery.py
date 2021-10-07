# class

class Parent():

    def __init__(self, name):
        self.name = name

    def p_method(self):
        print("parent")

class Child(Parent):

    def __init__(self):
        self.family = Cousin('surn')

class Cousin():

    def __init__(self, surname):
        self.surname = surname

    def c_method(self):
        print("hello")

mom = Parent('Mrs')
cuz = Cousin('Robins')
kid = Child()
kid.family.c_method()
kid.p_method()




