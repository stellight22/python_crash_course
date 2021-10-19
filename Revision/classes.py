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


model = Model('flower')
red = Supra('red')

red.s()
model.m()
model.s()
