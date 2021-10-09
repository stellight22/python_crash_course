import time

start = time.time()

from random import randint

class Die():
    def __init__(self, sides = 6):
        self.sides = sides

    def roll_die(self):
        r = randint(1, self.sides)
        print(f"your roll:{r}, sides: {self.sides}")

d = Die()

x = 1
while x < 11:
    d.roll_die()
    x += 1

print(time.time() - start)