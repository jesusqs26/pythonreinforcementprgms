from abc import ABC, abstractmethod
import time
import comms

class Programa(ABC):
    def __init__(self, reward, generadorNum, numDevice):
        self.comms = comms.Communication(numDevice)
        self.reward = reward
        self.generadorNum = generadorNum
        self.reporte = dict()
    
    @abstractmethod
    def comenzarPrograma(self):
        pass

    def ejecutarPrograma(self, duracion):
        tiempoInicial = time.time()
        while(duracion > (time.time() - tiempoInicial)):
            self.comenzarPrograma()
    
    
