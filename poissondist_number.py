import numpy

class PoissonDistributionNumber():

    def __init__(self, mean, estDev):
        self.mean = mean
        self.estDev = estDev

    def generateNumber(self):
        return numpy.random.poisson(self.mean, self.estDev)