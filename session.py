import programa, programa_intervalo, programa_razon, time


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

            
                
        
