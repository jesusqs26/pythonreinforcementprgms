import time
import comms
import programa

# Clase utilizada para ejecutar un programa de reforzamiento por razon
class ProgramaRazon(programa.Programa):

    # Metodo encargado de comenzar el programa de reforzamiento 
    def comenzarPrograma(self):
        razon = self.generadorNum.generateNumber() # Se genera una razon
        contador = 0 # Se inicializa un contador para determinar el progreso hacia cumplir la razon
        self.reporte["programtype"] =  "reason"
        self.reporte["reasons"].append({
            "time": time.time(),
            "reason": razon,
        })
        # Mientras tengamos una razon sin cumplir, no entregamos alimento y se esperan respuestas hasta cumplir la razon
        while(contador < razon):
            if(self.comms.readMessage()[0] == 1):
                self.reporte["responses"].append({
                    "time": time.time(),
                    "reward": 0
                })
                contador += 1
        # Se espera una respuesta para cumplir la razon y entregar alimento
        while(True):
            if(self.comms.readMessage()[0] == 1):
                self.reporte["responses"].append({
                    "time": time.time(),
                    "reward": self.reward
                })
                self.comms.doAction(self.reward)
                print(self.reporte)
                return