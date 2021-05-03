# Author: Jesús Ricardo Quintero Serrano
import serial
# import msvcrt       # No es necesario si no se utiliza el teclado para hacer algo
import serial.tools.list_ports
import logging
from datetime import datetime
import time

# Clase encargada de recibir datos del arduino y mandarle instrucciones
class Communication:
    def __init__(self, numDevice):
        # - Variables -
        self.arduino = serial.Serial(self.findArduino(numDevice), 9600)
        self.arduino.readline()
        

    # Detecta el puerto serial en el que se conecto el arduino //aun no valida que solo exista un arduino conectado
    def findArduino(self, numDevice):
        ports = serial.tools.list_ports.comports()
        commPort = 'None'
        numConnection = len(ports)

        for i in range(0,numConnection):
            port = ports[i]
            strPort = str(port)

            # Se valida si la descripcion es de arduino original o clon
            if 'USB-SERIAL CH340' in strPort or 'Arduino' in strPort:
                splitPort = strPort.split(' ')
                commPort = splitPort[numDevice]
        return commPort



    # Lee los datos del arduino del puerto serial y los regresa en una lista
    def readMessage(self):
        mensaje = self.arduino.readline()[:-2]
        datos = [int(x) for x in str(mensaje.decode("utf-8"))]
        return datos

    # Manda una instruccion de dispensar comida segun el numero al arduino (El arduino
    # debera estar programado para recibir un numero y dispensar la cantidad de comida correspondiente)
    def doAction(self, action):
        self.arduino.write(bytes(action))

    # Prende o apaga el led dependiendo del parametro state (true o false)
    def setLedState(self, state):
        if state:
            self.arduino.write(b'o')
        else:
            self.arduino.write(b'x')



    
    
