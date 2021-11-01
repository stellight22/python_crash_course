class Supra():

    def __init__(self, color):
        self.color = color

    def s(self):
        print(self.color)


class Model(Supra):

    def __init__(self, color):
        super().__init__(color)
        

    def m(self):
        print(self.color)



red = Supra('red')
model = Model('grey')

red.s()
model.m()
model.s()
