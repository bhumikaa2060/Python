import random
# numbers= [1,2,3,4,5,6]
# dice= random.choices(numbers, k=2)
# print(dice)

# class dice:
#
#     def roll(self, number):
#         self.number= random.choices(number, k=2)
#         return self.number
# diceclass = dice()
# numbers=(1,2,3,4,5,6)
# value= diceclass.roll(numbers)
# print(value)

class Dice:
    def roll(self):
        first =  random.randint(1,6)
        second = random.randint(1,6)
        return first, second #if no bracket then automatically becomes tuple


dice = Dice()
print(dice.roll())
