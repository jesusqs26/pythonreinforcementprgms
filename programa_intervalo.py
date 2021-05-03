import time
import comms
import programa

# Clase utilizada para ejecutar un programa de reforzamiento por intervalos
class ProgramaIntervalo(programa.Programa):

    # Metodo encargado de comenzar el programa de reforzamiento 
    def comenzarPrograma(self):
        intervalLength = self.generadorNum.generateNumber()
        intervalStart = time.time()
        intervalEnd = intervalStart + intervalLength
        self.reporte["intervals"].append({
            "length": intervalLength,
            "start": intervalStart,
            "end": intervalEnd
        })
        # Mientras tengamos un intervalo activo, no entregamos alimento y se esperan respuestas
        while(time.time() <= intervalEnd):
            if(self.comms.readMessage()[0] == 1):
                self.reporte["responses"].append({
                    "time": time.time(),
                    "reward": 0
                })
        # Se espera una respuesta al acabar el intervalo, para entregar alimento y generar otro intervalo
        while(True):
            if(self.comms.readMessage()[0] == 1):
                self.reporte["responses"].append({
                    "time": time.time(),
                    "reward": self.reward
                })
                self.comms.doAction(self.reward)
                print(self.reporte)
                return