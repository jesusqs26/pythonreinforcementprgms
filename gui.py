#
# Interfaz grafica del programa de riego automatico en python
#
# Jesus Ricardo Quintero Serrano 144454
#
from programa_razon import ProgramaRazon
from poissondist_number import PoissonDistributionNumber
from normaldist_number import NormalDistributionNumber
from fixed_number import FixedNumber
from random_number import RandomNumber
from programa_intervalo import ProgramaIntervalo
from session import Sesion
from tkinter import *
import programa
import time

# Clase de cuadro de dialogo usado para captrurar el nombre(frame) de la sesion
class popupWindow(object):
    def __init__(self,master):
        top=self.top=Toplevel(master)
        top.geometry("250x100")
        self.l=Label(top,text="Nombre de la sesion")
        self.l.pack()
        self.e=Entry(top)
        self.e.pack()
        self.l2=Label(top,text="Duración de la sesión")
        self.l2.pack()
        self.e2=Entry(top)
        self.e2.pack()
        self.b=Button(top,text='Ok',command=self.cleanup)
        self.b.pack()
    def cleanup(self):
        setDatosSesion(self.e.get(), self.e2.get())
        self.top.destroy()

# Declarando variables de la logica del programa
tiposdeprograma = [
    "Programa de intervalo fijo",
    "Programa de intervalo variable",
    "Programa de razón fija",
    "Programa de razón variable"
]
generadoresnumericos = [
    "Distribución Normal",
    "Distribución de Poisson",
    "Random: Semilla Meisser Twister"
]
tipoprograma_seleccion = None
generadoresnumericos_seleccion = None
value_label_text = None

sesion = None
nombresesion = None
duracionsesion = None
tipodeprograma = None
programa1 = None
programa2 = None

value_entry = None
desvEst_entry = None

# Funciones
# Funcion que comienza la entrada de parametros de la nueva sesion
def iniciarNuevaSesion():
    dialog = popupWindow(root)
    tiposesion_frame.pack(fill="both", expand=1)

# Funcion que establece un programa simple 
def programasimple_boton():
    tiposesion_frame.destroy()
    tipodeprograma = 's'
    programa_frame.pack(fill="both", expand=1)

# Funcion que establece un programa comcurrente 
def programaconcurrente_boton():
    tiposesion_frame.destroy()
    tipodeprograma = 'c'
    programa_frame.pack(fill="both", expand=1)

# Funcion que establece el tipo de programa cuando se presiona el boton aceptar
def tipodeprograma_boton_aceptar():
    pass
        
            
def seleccion_tipodeprograma_combobox(event):
    if(tipoprograma_seleccion.get()=="Programa de intervalo fijo" or tipoprograma_seleccion.get()=="Programa de razón fija"):
        generadornumerico_label.grid_forget()
        generadornumerico_combobox.grid_forget()
        media_label.grid_forget()
        desvEst_label.grid_forget()
        desvEst_entry.grid_forget()
    elif(tipoprograma_seleccion.get()=="Programa de intervalo variable" or tipoprograma_seleccion.get()=="Programa de razón variable"):
        generadornumerico_label.grid(row=2,column=1)
        generadornumerico_combobox.grid(row=3,column=1)
        media_label.grid(row=5,column=1)
        desvEst_label.grid(row=7,column=1)
        desvEst_entry.grid(row=8,column=1)
    

    if(generadoresnumericos_seleccion.get().startswith("Random")):
        media_label_text.set("Primer Numero")
        desvEst_label_text.set("Segundo Numero")
    else:
        media_label_text.set("Media")
        if(tipoprograma_seleccion.get().startswith("Programa de intervalo")):
            value_label_text.set("Intervalo")
        else:
            value_label_text.set("Razón")
        desvEst_label_text.set("Desviación Estandar")
        

def aceptarPrograma():
    if(tipodeprograma == 's'):
        if(tipoprograma_seleccion.get().startswith("Programa de intervalo fijo")):           
            programa1 = ProgramaIntervalo(1,FixedNumber(value_entry.get()),0)
        elif(tipoprograma_seleccion.get().startswith("Programa de intervalo variable")):
            if(generadoresnumericos_seleccion.get()=="Distribución Normal"):
                programa1 = ProgramaIntervalo(1,NormalDistributionNumber(value_entry.get(),desvEst_entry.get()),0)
            elif(generadoresnumericos_seleccion.get()=="Distribución de Poisson"):
                programa1 = ProgramaIntervalo(1,PoissonDistributionNumber(value_entry.get(),desvEst_entry.get()),0)
            elif(generadoresnumericos_seleccion.get().startswith("Random")):
                programa1 = ProgramaIntervalo(1,RandomNumber(value_entry.get(), desvEst_entry.get()),0)
        elif(tipoprograma_seleccion.get().startswith("Programa de razón fija")):
            programa1 = ProgramaRazon(1,FixedNumber(value_entry.get()),0)
        elif(tipoprograma_seleccion.get().startswith("Programa de razón variable")):
            if(generadoresnumericos_seleccion.get()=="Distribución Normal"):
                programa1 = ProgramaRazon(1,NormalDistributionNumber(value_entry.get(),desvEst_entry.get()),0)
            elif(generadoresnumericos_seleccion.get()=="Distribución de Poisson"):
                programa1 = ProgramaRazon(1,PoissonDistributionNumber(value_entry.get(),desvEst_entry.get()),0)
            elif(generadoresnumericos_seleccion.get().startswith("Random")):
                programa1 = ProgramaRazon(1,RandomNumber(value_entry.get(), desvEst_entry.get()),0)
    else:
        if(programa1 is not None):
            if(tipoprograma_seleccion.get().startswith("Programa de intervalo fijo")):           
                programa1 = ProgramaIntervalo(1,FixedNumber(value_entry.get()),0)
            elif(tipoprograma_seleccion.get().startswith("Programa de intervalo variable")):
                if(generadoresnumericos_seleccion.get()=="Distribución Normal"):
                    programa1 = ProgramaIntervalo(1,NormalDistributionNumber(value_entry.get(),desvEst_entry.get()),0)
                elif(generadoresnumericos_seleccion.get()=="Distribución de Poisson"):
                    programa1 = ProgramaIntervalo(1,PoissonDistributionNumber(value_entry.get(),desvEst_entry.get()),0)
                elif(generadoresnumericos_seleccion.get().startswith("Random")):
                    programa1 = ProgramaIntervalo(1,RandomNumber(value_entry.get(), desvEst_entry.get()),0)
            elif(tipoprograma_seleccion.get().startswith("Programa de razón fija")):
                programa1 = ProgramaRazon(1,FixedNumber(value_entry.get()),0)
            elif(tipoprograma_seleccion.get().startswith("Programa de razón variable")):
                if(generadoresnumericos_seleccion.get()=="Distribución Normal"):
                    programa1 = ProgramaRazon(1,NormalDistributionNumber(value_entry.get(),desvEst_entry.get()),0)
                elif(generadoresnumericos_seleccion.get()=="Distribución de Poisson"):
                    programa1 = ProgramaRazon(1,PoissonDistributionNumber(value_entry.get(),desvEst_entry.get()),0)
                elif(generadoresnumericos_seleccion.get().startswith("Random")):
                    programa1 = ProgramaRazon(1,RandomNumber(value_entry.get(), desvEst_entry.get()),0)

            tiposesionFrame_label_text.set("Parametros para el programa 2")
        else:
            if(tipoprograma_seleccion.get().startswith("Programa de intervalo fijo")):           
                programa2 = ProgramaIntervalo(1,FixedNumber(value_entry.get()),0)
            elif(tipoprograma_seleccion.get().startswith("Programa de intervalo variable")):
                if(generadoresnumericos_seleccion.get()=="Distribución Normal"):
                    programa2 = ProgramaIntervalo(1,NormalDistributionNumber(value_entry.get(),desvEst_entry.get()),0)
                elif(generadoresnumericos_seleccion.get()=="Distribución de Poisson"):
                    programa2 = ProgramaIntervalo(1,PoissonDistributionNumber(value_entry.get(),desvEst_entry.get()),0)
                elif(generadoresnumericos_seleccion.get().startswith("Random")):
                    programa2 = ProgramaIntervalo(1,RandomNumber(value_entry.get(), desvEst_entry.get()),0)
            elif(tipoprograma_seleccion.get().startswith("Programa de razón fija")):
                programa2 = ProgramaRazon(1,FixedNumber(value_entry.get()),0)
            elif(tipoprograma_seleccion.get().startswith("Programa de razón variable")):
                if(generadoresnumericos_seleccion.get()=="Distribución Normal"):
                    programa2 = ProgramaRazon(1,NormalDistributionNumber(value_entry.get(),desvEst_entry.get()),0)
                elif(generadoresnumericos_seleccion.get()=="Distribución de Poisson"):
                    programa2 = ProgramaRazon(1,PoissonDistributionNumber(value_entry.get(),desvEst_entry.get()),0)
                elif(generadoresnumericos_seleccion.get().startswith("Random")):
                    programa2 = ProgramaRazon(1,RandomNumber(value_entry.get(), desvEst_entry.get()),0)
            

def setDatosSesion(nombresesion, duracion):
    nombresesion = nombresesion
    duracionsesion = duracion


# Ventana de la app
root = Tk()
root.title('Sesiones experimentales de condicionamiento operante')
root.geometry("400x400")




# Declarando el menu principal
my_menu = Menu(root)
root.config(menu=my_menu)

# Declarando categoria de menu "Sesion"
sesion_menu = Menu(my_menu)
my_menu.add_cascade(label="Sesion", menu=sesion_menu)

# Opciones de la categoria de sesion
sesion_menu.add_command(label="Nueva Sesion", command=iniciarNuevaSesion)
sesion_menu.add_separator()
sesion_menu.add_command(label="Exit", command=root.quit)

# Frames
# Frame de seleccion de tipo de sesion
tiposesionFrame_label_text = StringVar()
tiposesionFrame_label_text.set("Parametros para el programa 1")
tiposesion_frame = LabelFrame(root, text="Parametros para el programa 1", padx=5, pady=5)
programasimple_boton=Button(tiposesion_frame, text="Programa simple(1 programa)", command=programasimple_boton)
programaconcurrente_boton=Button(tiposesion_frame, text="Programas concurrente(2 programas)", command=None)
programasimple_boton.pack()
programaconcurrente_boton.pack()
#Frame de entrada de parametros de programa
programa_frame = LabelFrame(root, text="Parametros del programa", pady=5, padx=5)
programa_frame.columnconfigure(1, weight=2)
tipoprograma_seleccion = StringVar()
tipoprograma_seleccion.set(tiposdeprograma[0])
tipoprograma_label = Label(programa_frame, text="Tipo de programa")
tipoprograma_combobox = OptionMenu(programa_frame, tipoprograma_seleccion, *tiposdeprograma, command=seleccion_tipodeprograma_combobox)
tipoprograma_aceptar_boton =Button(programa_frame, text="Aceptar", command=aceptarPrograma)
generadoresnumericos_seleccion = StringVar()
generadoresnumericos_seleccion.set(generadoresnumericos[0])
generadornumerico_label = Label(programa_frame, text="Generador Numerico")
generadornumerico_combobox = OptionMenu(programa_frame, generadoresnumericos_seleccion, *generadoresnumericos, command=seleccion_tipodeprograma_combobox)
value_label_text = StringVar()
value_label_text.set("Intervalo")
desvEst_label_text = StringVar()
desvEst_label_text.set("Desviación Estandar")
media_label_text = StringVar()
media_label_text.set("Media")
value_label = Label(programa_frame, textvariable=value_label_text)
value_entry = Entry(programa_frame)
media_label = Label(programa_frame, textvariable=media_label_text)
desvEst_label = Label(programa_frame, textvariable=desvEst_label_text)
desvEst_entry = Entry(programa_frame)
tipoprograma_label.grid(row=0,column=1)
tipoprograma_combobox.grid(row=1,column=1)
value_label.grid(row=4,column=1)
media_label.grid(row=5,column=1)
value_entry.grid(row=6,column=1)
desvEst_label.grid(row=7,column=1)
desvEst_entry.grid(row=8,column=1)
tipoprograma_aceptar_boton.grid(row=12, column=1)
# Frame de programa en curso
monitoreo_frame = LabelFrame(root, text="Programa en curso", pady=5, padx=5)
programa_frame.columnconfigure(1, weight=2)
contador_tiempo = StringVar()
contador_respuestas = StringVar()
contador_refuerzos = StringVar()
tiempo_label = Label(monitoreo_frame, text="Tiempo: ")
respuestas_label = Label(monitoreo_frame, text="Respuestas acumuladas: ")
refuerzos_label = Label(monitoreo_frame, text="Refuerzos entregados: ")
valortiempo_label = Label(monitoreo_frame, textvariable=contador_tiempo)
valorrespuestas_label = Label(monitoreo_frame, textvariable=contador_respuestas)
valorrefuerzos_label = Label(monitoreo_frame, textvariable=contador_refuerzos)
valortiempo_label.grid(row=0,column=1)
valorrespuestas_label.grid(row=1, column=1)
valorrefuerzos_label.grid(row=2, column=1)
tiempo_label.grid(row=0,column=0)
respuestas_label.grid(row=1, column=0)
refuerzos_label.grid(row=2, column=0)
monitoreo_frame.pack()


root.mainloop()

