import random

class RandomNumber():

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    
    def generateNumber(self):
        return random.randint(self.num1, self.num2)