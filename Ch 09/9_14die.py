#9-14 random dice function
from random import randint
d = randint(1,6)
print("A randomly generated integer from 1 to 6 is: " +str(d))

class Die:
    def __init__(self, sides =6):
        self.sides = sides

    def roll_die(self):
        #returns a number in between 1 and #sides
        return randint(1,self.sides)

#regular 6-sided dice
d1 = Die()
d1.roll_die()

#10 rolls of d1
#need a list to store results

recorded_rolls = []
for x in range(10):
    record = d1.roll_die()
    recorded_rolls.append(record)
print("10 rolls of a 6-sided die:")
print(recorded_rolls)

#10-sided die
d2 = Die(sides= 10)
recorded_10 = []
for n in range(10):
    record = d2.roll_die()
    recorded_10.append(record)
print("\n 10 rolls of a 10-sided die will produce: ")
print(recorded_10)

#20-sided die
d20 = Die(sides = 20)
recorded_20 = []
for y in range(10):
    record = d20.roll_die()
    recorded_20.append(record)
print("\n The result of rolling a 20-sided die 20x: ")
print(recorded_20)