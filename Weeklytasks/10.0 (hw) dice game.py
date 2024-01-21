# 11.1 HOUR 1 LECTURE - help on the dice game. 
# how many sides there are on a dice: 

# # import random integers -->
# from random import randrange
# print(randrange(10))

# class Dice:
#     sides = 6 
# # if you see something where the first letter is capitalised it is most likely a class 
# # the class defines the shape/blueprint
#     def __init__(self, sides):
#         self.sides = sides 
#         # defined the initulizar function, self is the internal 
#     def roll(self): 
#         return randrange(self.sides) + 1
#     # range from 0-5 it gets shifted one 

# class Dices: 
#     dices = []
#     def roll(self): 

# dice = Dice(8)
# print(dice.roll())

# basically the properties is the class and sides, then the methods are where def is. 



from random import randrange
class Dice:
    sides = 6 

    def __init__(self,sides): 
        self.sides = sides 

    def roll(self): 
        return randrange(self.sides) + 1 
    
class Dices:
    dices = []

    def __init__(self,number,sides):
        for i in range(number):
            self.dices.append(Dice(sides))
    
    def roll(self): 
        result = []
        for dice in self.dices: 
            result.append(dice.roll())
        return result

peices = Dices(4,6)
print(peices.roll())

