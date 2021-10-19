class Super():
    def __init__(self, age):
        self.age = age

    def method_rock(self):
        print(self.age)


class Baby(Super):
    def __init__(self, age):
        super().__init__(age)

    def method_scissors(self):
        print(self.age)


s1 = Super(22)
s1.method_rock()
b1 = Baby(55)
b1.method_scissors()
b1.method_rock()