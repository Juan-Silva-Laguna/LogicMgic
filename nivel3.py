import tkinter as tk
from tkinter import ttk
import pygame
import random

class Nivel3(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.nombre_label= tk.Label(parent, text="Bienvenido(a) a el Tercer Nivel, en este nivel tendras que hacer algunas operaciones con total concentracion, para que podamos entrar a tu mente y lograr adivinar tu fecha de nacimiento. ¿Estas listo(a)?", wraplength=150)
        self.btn=tk.Button(self.parent, text="Si, estoy Listo",width="20",height="1",command=self.mostrarTexto1,bg="indian red",fg="white")
        self.num1 = random.randint(3, 10)
        self.num2 = random.randint(50, 300)
        self.num3 = random.randint(1, 4)
        self.input1 = tk.Entry(self.parent)
        self.input2 = tk.Entry(self.parent)
        self.input3 = tk.Entry(self.parent)
        self.val1 = 0
        self.val2 = 0
        self.val3 = 0
        self.nombre_label.place(x=80,y=10)
        self.btn.place(x=80,y=160)
    
    def mostrarTexto1(self):
        self.nombre_label.destroy()
        self.btn.destroy()
        self.nombre_label= tk.Label(self.parent, text="Tu dia de tu nacimiento multiplicalo por "+str(self.num1), wraplength=150)
        self.btn=tk.Button(self.parent, text="Listo",width="20",height="1",command=self.mostrarTexto2,bg="indian red",fg="white")
        self.nombre_label.place(x=80,y=10)
        self.btn.place(x=80,y=100)

    def mostrarTexto2(self):
        self.nombre_label.destroy()
        self.btn.destroy()
        self.nombre_label = tk.Label(self.parent, text="Igresa el resultado de la operacion anterior", wraplength=150)
        self.btn=tk.Button(self.parent, text="Listo",width="20",height="1",command=self.mostrarTexto3,bg="indian red",fg="white")
        self.nombre_label.place(x=80,y=10)
        self.input1.place(x=80,y=100)
        self.btn.place(x=80,y=140)
    
    def mostrarTexto3(self):
        self.nombre_label.destroy()
        self.btn.destroy()
        self.val1 = self.input1.get()
        self.input1.destroy()
        self.nombre_label= tk.Label(self.parent, text="A tu mes de tu nacimiento sumale "+str(self.num2), wraplength=150)
        self.btn=tk.Button(self.parent, text="Listo",width="20",height="1",command=self.mostrarTexto4,bg="indian red",fg="white")
        self.nombre_label.place(x=80,y=10)
        self.btn.place(x=80,y=100)

    def mostrarTexto4(self):
        self.nombre_label.destroy()
        self.btn.destroy()
        self.nombre_label = tk.Label(self.parent, text="Igresa el resultado de la operacion anterior", wraplength=150)
        self.btn=tk.Button(self.parent, text="Listo",width="20",height="1",command=self.mostrarTexto5,bg="indian red",fg="white")
        self.nombre_label.place(x=80,y=10)
        self.input2.place(x=80,y=100)
        self.btn.place(x=80,y=140)

    def mostrarTexto5(self):
        self.nombre_label.destroy()
        self.btn.destroy()
        self.val2 = self.input2.get()
        self.input2.destroy()
        self.nombre_label= tk.Label(self.parent, text="A el año de tu nacimiento multiplicalo por "+str(self.num3), wraplength=150)
        self.btn=tk.Button(self.parent, text="Listo",width="20",height="1",command=self.mostrarTexto6,bg="indian red",fg="white")
        self.nombre_label.place(x=80,y=10)
        self.btn.place(x=80,y=100)

    def mostrarTexto6(self):
        self.nombre_label.destroy()
        self.btn.destroy()
        self.nombre_label = tk.Label(self.parent, text="Igresa el resultado de la operacion anterior", wraplength=150)
        self.btn=tk.Button(self.parent, text="Listo",width="20",height="1",command=self.calcular,bg="indian red",fg="white")
        self.nombre_label.place(x=80,y=10)
        self.input3.place(x=80,y=100)
        self.btn.place(x=80,y=140)

    def calcular(self):
        self.nombre_label.destroy()
        self.btn.destroy()
        self.val3 = self.input3.get()
        self.input3.destroy()

        dia = int(int(self.val1)/self.num1)
        mes = int(self.val2)-self.num2
        agno = int(int(self.val3)/self.num3)

        self.nombre_label = tk.Label(self.parent, text="Segun el procedimiento y si hiciste todas las operaciones con atención, podemos decir con total seguridad que la fecha de tu nacimiento es: "+str(dia)+"/"+str(mes)+"/"+str(agno), wraplength=150)
        self.btn=tk.Button(self.parent, text="Salir",width="20",height="1",command=self.cerrar,bg="indian red",fg="white")
        self.nombre_label.place(x=80,y=10)
        self.btn.place(x=80,y=130)

    def cerrar(self):
        pygame.mixer.init()
        pygame.mixer.music.load("C:/Users/juanc/OneDrive/Documentos/PROYECTOS/Python/LogigMagic/music/aplausos.mp3")
        pygame.mixer.music.play()
        self.parent.destroy()