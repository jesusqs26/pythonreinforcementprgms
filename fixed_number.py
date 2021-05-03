import generador_numerico

class FixedNumber(generador_numerico.GeneradorNumerico):

    def __init__(self, number):
        self.number = number

    def generateNumber(self):
        return self.number
