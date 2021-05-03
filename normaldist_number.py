import numpy
import generador_numerico

class NormalDistributionNumber(generador_numerico.GeneradorNumerico):

    def __init__(self, mean, estDev):
        self.mean = mean
        self.estDev = estDev

    def generateNumber(self):
        return numpy.random.normal(self.mean, self.estDev)