import programa, programa_intervalo, programa_razon
import time
import threading


class Sesion():

    def __init__(self, sessionid, sessionLength):
        self.sessionid = sessionid
        self.sessionLength = sessionLength
        self.report = dict()
        self.programs = list<programa.Programa>()

    # Metodo encargado de generar un reporte en formato JSON
    def createReport(self):
        self.report = {
            "Frame": self.sessionid,
            "Duracion": self.sessionLength,
            "Hora de inicio de la sesion": time.time(),
            "Programas": [

            ]
            
        }
        for n in range(self.programs):
            self.report["Programas"].append({n: self.programs[n]})

    
    # Metodo encargado de inicializar los programas de reforzamiento a reproducir
    def setProgramasDeReforzamiento(self, programa1, programa2):
        # Limpio la lista
        self.programs = list<programa.Programa>()
        
        if(programa2 != None):
            self.programs.append(programa1)
            self.programs.append(programa2)
        else:   # Si solo hay un programa de reforzamiento, se agrega programa1 solamente
            self.programs.append(programa1)

    

                
        
