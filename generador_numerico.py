from abc import ABC, abstractmethod

# Interfaz utilizada para implementar un generador de numero a partir de parametros
class GeneradorNumerico(ABC):

    @abstractmethod
    def generateNumber(self):
        pass