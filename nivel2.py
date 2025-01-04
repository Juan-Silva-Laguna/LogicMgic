import tkinter as tk
from tkinter import ttk
import pygame
import random

class Nivel2(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.nombre_label= tk.Label(parent, text="Bienvenido(a) a el Segundo Nivel, en este nivel tendras que hacer algunas operaciones con total concentracion, para que podamos entrar a tu mente y lograr adivinar tu numero celular. ¿Estas listo(a)?", wraplength=150)
        self.btn=tk.Button(self.parent, text="Si, estoy Listo",width="20",height="1",command=self.mostrarTexto2,bg="indian red",fg="white")
        self.num1 = random.randint(200, 700)
        self.num2 = random.randint(1, 200)
        self.num3 = random.randint(200, 700)
        self.input1 = tk.Entry(self.parent)
        self.nombre_label.place(x=80,y=10)
        self.btn.place(x=80,y=160)
    
    def mostrarTexto2(self):
        self.nombre_label.destroy()
        self.btn.destroy()
        self.nombre_label= tk.Label(self.parent, text="A tu numero de celular sumale "+str(self.num1), wraplength=150)
        self.btn=tk.Button(self.parent, text="Listo",width="20",height="1",command=self.mostrarTexto3,bg="indian red",fg="white")
        self.nombre_label.place(x=80,y=10)
        self.btn.place(x=80,y=100)
    
    def mostrarTexto3(self):
        self.nombre_label.destroy()
        self.btn.destroy()
        self.nombre_label= tk.Label(self.parent, text="Al resultado anterior restale "+str(self.num2), wraplength=150)
        self.btn=tk.Button(self.parent, text="Listo",width="20",height="1",command=self.mostrarTexto4,bg="indian red",fg="white")
        self.nombre_label.place(x=80,y=10)
        self.btn.place(x=80,y=100)
    
    def mostrarTexto4(self):
        self.nombre_label.destroy()
        self.btn.destroy()
        self.nombre_label= tk.Label(self.parent, text="Al resultado anterior sumale "+str(self.num3), wraplength=150)
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
        total = int(entrada)-((self.num1+self.num3)-self.num2)
        self.nombre_label = tk.Label(self.parent, text="Segun el procedimiento y si hiciste todas las operaciones con atención, podemos decir con total seguridad que tu numero de ceular es: "+str(total), wraplength=150)
        self.btn=tk.Button(self.parent, text="Salir",width="20",height="1",command=self.cerrar,bg="indian red",fg="white")
        self.nombre_label.place(x=80,y=10)
        self.btn.place(x=80,y=130)

    def cerrar(self):
        pygame.mixer.init()
        pygame.mixer.music.load("C:/Users/juanc/OneDrive/Documentos/PROYECTOS/Python/LogigMagic/music/aplausos.mp3")
        pygame.mixer.music.play()
        self.parent.destroy()