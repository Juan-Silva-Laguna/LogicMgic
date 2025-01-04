import tkinter as tk
from tkinter import ttk
import pygame

class Nivel6(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.nombre_label= tk.Label(parent, text="Bienvenido(a) a el Sexto Nivel, en este nivel tendras que hacer algunas operaciones con total concentracion, para que podamos entrar a tu mente y lograr adivinar la talla de zapatos. ¿Estas listo(a)?", wraplength=150)
        self.btn=tk.Button(self.parent, text="Si, estoy Listo",width="20",height="1",command=self.mostrarTexto1,bg="indian red",fg="white")
        self.input1 = tk.Entry(self.parent)
        self.nombre_label.place(x=80,y=10)
        self.btn.place(x=80,y=160)
    
    def mostrarTexto1(self):
        self.nombre_label.destroy()
        self.btn.destroy()
        self.nombre_label= tk.Label(self.parent, text="La talla de tus zapatos multiplicala por 5", wraplength=150)
        self.btn=tk.Button(self.parent, text="Listo",width="20",height="1",command=self.mostrarTexto2,bg="indian red",fg="white")
        self.nombre_label.place(x=80,y=10)
        self.btn.place(x=80,y=100)
    
    def mostrarTexto2(self):
        self.nombre_label.destroy()
        self.btn.destroy()
        self.nombre_label= tk.Label(self.parent, text="Ahora sumale 50 ", wraplength=150)
        self.btn=tk.Button(self.parent, text="Listo",width="20",height="1",command=self.mostrarTexto3,bg="indian red",fg="white")
        self.nombre_label.place(x=80,y=10)
        self.btn.place(x=80,y=100)
    
    def mostrarTexto3(self):
        self.nombre_label.destroy()
        self.btn.destroy()
        self.nombre_label= tk.Label(self.parent, text="Al resultado anterior multiplicalo por 20 ", wraplength=150)
        self.btn=tk.Button(self.parent, text="Listo",width="20",height="1",command=self.mostrarTexto4,bg="indian red",fg="white")
        self.nombre_label.place(x=80,y=10)
        self.btn.place(x=80,y=100)
    
    def mostrarTexto4(self):
        self.nombre_label.destroy()
        self.btn.destroy()
        self.nombre_label= tk.Label(self.parent, text="Al resultado anterior sumale 1015", wraplength=150)
        self.btn=tk.Button(self.parent, text="Listo",width="20",height="1",command=self.mostrarTexto5,bg="indian red",fg="white")
        self.nombre_label.place(x=80,y=10)
        self.btn.place(x=80,y=100)
    
    def mostrarTexto5(self):
        self.nombre_label.destroy()
        self.btn.destroy()
        self.nombre_label= tk.Label(self.parent, text="Al resultado anterior restale tu año de nacmiento", wraplength=150)
        self.btn=tk.Button(self.parent, text="Listo",width="20",height="1",command=self.mostrarTexto6,bg="indian red",fg="white")
        self.nombre_label.place(x=80,y=10)
        self.btn.place(x=80,y=100)

    def mostrarTexto6(self):
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
        talla = entrada[:2]
        self.nombre_label = tk.Label(self.parent, text="Segun el procedimiento y si hiciste todas las operaciones con atención, podemos decir con total seguridad que la talla de tuz zapatos es "+str(talla), wraplength=150)
        self.btn=tk.Button(self.parent, text="Salir",width="20",height="1",command=self.cerrar,bg="indian red",fg="white")
        self.nombre_label.place(x=80,y=10)
        self.btn.place(x=80,y=130)

    def cerrar(self):
        pygame.mixer.init()
        pygame.mixer.music.load("C:/Users/juanc/OneDrive/Documentos/PROYECTOS/Python/LogigMagic/music/aplausos.mp3")
        pygame.mixer.music.play()
        self.parent.destroy()