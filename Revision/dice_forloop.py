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

for x in range(1,11):
    d.roll_die()

print(time.time() - start)