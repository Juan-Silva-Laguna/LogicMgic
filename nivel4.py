import tkinter as tk
from tkinter import ttk
import pygame
import random

class Nivel4(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.nombre_label= tk.Label(parent, text="Bienvenido(a) a el Cuarto Nivel, en este nivel tendras que hacer algunas operaciones con total concentracion, para que podamos entrar a tu mente y lograr adivinar tu edad. ¿Estas listo(a)?", wraplength=150)
        self.btn=tk.Button(self.parent, text="Si, estoy Listo",width="20",height="1",command=self.mostrarTexto1,bg="indian red",fg="white")
        self.input1 = tk.Entry(self.parent)
        self.nombre_label.place(x=80,y=10)
        self.btn.place(x=80,y=160)
        self.meses = {
            1: "Enero",
            2: "Febrero",
            3: "Marzo",
            4: "Abril",
            5: "Mayo",
            6: "Junio",
            7: "Julio",
            8: "Agosto",
            9: "Septiembre",
            10: "Octubre",
            11: "Noviembre",
            12: "Diciembre"
        }
    
    def mostrarTexto1(self):
        self.nombre_label.destroy()
        self.btn.destroy()
        self.nombre_label= tk.Label(self.parent, text="Multiplica tu mes de nacimiento por 2", wraplength=150)
        self.btn=tk.Button(self.parent, text="Listo",width="20",height="1",command=self.mostrarTexto2,bg="indian red",fg="white")
        self.nombre_label.place(x=80,y=10)
        self.btn.place(x=80,y=100)
    
    def mostrarTexto2(self):
        self.nombre_label.destroy()
        self.btn.destroy()
        self.nombre_label= tk.Label(self.parent, text="Ahora sumale 5 a el reultado anterior", wraplength=150)
        self.btn=tk.Button(self.parent, text="Listo",width="20",height="1",command=self.mostrarTexto3,bg="indian red",fg="white")
        self.nombre_label.place(x=80,y=10)
        self.btn.place(x=80,y=100)
    
    def mostrarTexto3(self):
        self.nombre_label.destroy()
        self.btn.destroy()
        self.nombre_label= tk.Label(self.parent, text="El resultado anterior multiplicalo por 50 ", wraplength=150)
        self.btn=tk.Button(self.parent, text="Listo",width="20",height="1",command=self.mostrarTexto4,bg="indian red",fg="white")
        self.nombre_label.place(x=80,y=10)
        self.btn.place(x=80,y=100)
    
    def mostrarTexto4(self):
        self.nombre_label.destroy()
        self.btn.destroy()
        self.nombre_label= tk.Label(self.parent, text="Por ultimo suma tu edad a el resultado anterior", wraplength=150)
        self.btn=tk.Button(self.parent, text="Listo",width="20",height="1",command=self.mostrarTexto5,bg="indian red",fg="white")
        self.nombre_label.place(x=80,y=10)
        self.btn.place(x=80,y=100)

    def mostrarTexto5(self):
        self.nombre_label.destroy()
        self.btn.destroy()
        self.nombre_label = tk.Label(self.parent, text="Igresa el resultado de las operaciones anteriores", wraplength=150)
        self.btn=tk.Button(self.parent, text="Listo",width="20",height="1",command=self.calcular,bg="indian red",fg="white")
        self.nombre_label.place(x=80,y=10)
        self.input1.place(x=80,y=100)
        self.btn.place(x=80,y=140)
    
    def calcular(self):
        self.nombre_label.destroy()
        self.btn.destroy()
        entrada = self.input1.get()
        self.input1.destroy()
        total = int(entrada)-250
        if len(str(total)) == 4:
            mes = str(total)[:2]
            edad = str(total)[2:]
        else:
            mes = str(total)[:1]
            edad = str(total)[1:]
            
        mes = self.meses.get(int(mes), "Mes inválido")
        self.nombre_label = tk.Label(self.parent, text="Segun el procedimiento y si hiciste todas las operaciones con atención, podemos decir con total seguridad que el mes en que naciste es "+mes+" y tienes "+edad+" años", wraplength=150)
        self.btn=tk.Button(self.parent, text="Salir",width="20",height="1",command=self.cerrar,bg="indian red",fg="white")
        self.nombre_label.place(x=80,y=10)
        self.btn.place(x=80,y=130)

    def cerrar(self):
        pygame.mixer.init()
        pygame.mixer.music.load("C:/Users/juanc/OneDrive/Documentos/PROYECTOS/Python/LogigMagic/music/aplausos.mp3")
        pygame.mixer.music.play()
        self.parent.destroy()