import tkinter as tk
import pygame
from nivel1 import Nivel1
from nivel2 import Nivel2
from nivel3 import Nivel3
from nivel4 import Nivel4
from nivel5 import Nivel5
from nivel6 import Nivel6

def sonidoBorbuja():
    pygame.mixer.init()
    pygame.mixer.music.load("C:/Users/juanc/Documents/MIS PROYECTOS/Python/Python/LogigMagic/music/borbuja.mp3")
    pygame.mixer.music.play()

def abrirPrimerNivel():
    sonidoBorbuja()
    ventanaN1 = tk.Tk()
    ventanaN1.title("NIVEL 1")
    ventanaN1.config(width=300, height=200)
    nivel1 = Nivel1(ventanaN1)
    ventanaN1.mainloop()

def abrirSegundoNivel():
    sonidoBorbuja()
    ventanaN2 = tk.Tk()
    ventanaN2.title("NIVEL 2")
    ventanaN2.config(width=300, height=200)
    nivel2 = Nivel2(ventanaN2)
    ventanaN2.mainloop()

def abrirTercerNivel():
    sonidoBorbuja()
    ventanaN3 = tk.Tk()
    ventanaN3.title("NIVEL 3")
    ventanaN3.config(width=300, height=200)
    nivel3 = Nivel3(ventanaN3)
    ventanaN3.mainloop()

def abrirCuartoNivel():
    sonidoBorbuja()
    ventanaN4 = tk.Tk()
    ventanaN4.title("NIVEL 4")
    ventanaN4.config(width=300, height=200)
    nivel4 = Nivel4(ventanaN4)
    ventanaN4.mainloop()

def abrirQuintoNivel():
    sonidoBorbuja()
    ventanaN5 = tk.Tk()
    ventanaN5.title("NIVEL 5")
    ventanaN5.config(width=300, height=200)
    nivel5 = Nivel5(ventanaN5)
    ventanaN5.mainloop()

def abrirSextoNivel():
    sonidoBorbuja()
    ventanaN6 = tk.Tk()
    ventanaN6.title("NIVEL 6")
    ventanaN6.config(width=300, height=200)
    nivel6 = Nivel6(ventanaN6)
    ventanaN6.mainloop()

ventana = tk.Tk()

# Carga la imagen
primero_superior = tk.PhotoImage(file="C:/Users/juanc/Documents/MIS PROYECTOS/Python/Python/LogigMagic/img/uno.png")
segundo_superior = tk.PhotoImage(file="C:/Users/juanc/Documents/MIS PROYECTOS/Python/Python/LogigMagic/img/dos.png")
tercero_superior = tk.PhotoImage(file="C:/Users/juanc/Documents/MIS PROYECTOS/Python/Python/LogigMagic/img/tres.png")
cuarto_inferior = tk.PhotoImage(file="C:/Users/juanc/Documents/MIS PROYECTOS/Python/Python/LogigMagic/img/cuatro.png")
quinto_inferior = tk.PhotoImage(file="C:/Users/juanc/Documents/MIS PROYECTOS/Python/Python/LogigMagic/img/cinco.png")
sexto_inferior = tk.PhotoImage(file="C:/Users/juanc/Documents/MIS PROYECTOS/Python/Python/LogigMagic/img/seis.png")

# Define las dimensiones deseadas para la imagen
width = 80
height = 80

# Redimensiona la imagen a las dimensiones especificadas
resized_segundo_superior = segundo_superior.subsample(segundo_superior.width() // width, segundo_superior.height() // height)
resized_primero_superior = primero_superior.subsample(primero_superior.width() // width, primero_superior.height() // height)
resized_tercero_superior = tercero_superior.subsample(tercero_superior.width() // width, tercero_superior.height() // height)
resized_cuarto_inferior = cuarto_inferior.subsample(cuarto_inferior.width() // width, cuarto_inferior.height() // height)
resized_quinto_inferior = quinto_inferior.subsample(quinto_inferior.width() // width, quinto_inferior.height() // height)
resized_sexto_inferior = sexto_inferior.subsample(sexto_inferior.width() // width, sexto_inferior.height() // height)

# Crea una etiqueta con la imagen
label_segundo_superior = tk.Label(ventana, image=resized_segundo_superior)
label_primero_superior = tk.Label(ventana, image=resized_primero_superior)
label_tercero_superior = tk.Label(ventana, image=resized_tercero_superior)
label_cuarto_inferior = tk.Label(ventana, image=resized_cuarto_inferior)
label_quinto_inferior = tk.Label(ventana, image=resized_quinto_inferior)
label_sexto_inferior = tk.Label(ventana, image=resized_sexto_inferior)

label_primero_superior.bind("<Button-1>", lambda event: abrirPrimerNivel())
label_segundo_superior.bind("<Button-1>", lambda event: abrirSegundoNivel())
label_tercero_superior.bind("<Button-1>", lambda event: abrirTercerNivel())
label_cuarto_inferior.bind("<Button-1>", lambda event: abrirCuartoNivel())
label_quinto_inferior.bind("<Button-1>", lambda event: abrirQuintoNivel())
label_sexto_inferior.bind("<Button-1>", lambda event: abrirSextoNivel())


# Agrega un título centrado al inicio
title_label = tk.Label(ventana, text="Geniecito", font=("Arial", 16, "bold"), foreground= "darkcyan")
title_label.grid(row=0, column=0, columnspan=3)
                 
# Posiciona las etiquetas en una cuadrícula
label_segundo_superior.grid(row=1, column=1, padx=10, pady=10)
label_primero_superior.grid(row=1, column=0, padx=10, pady=10)
label_tercero_superior.grid(row=1, column=2, padx=10, pady=10)
label_cuarto_inferior.grid(row=2, column=0, padx=10, pady=10)
label_quinto_inferior.grid(row=2, column=1, padx=10, pady=10)
label_sexto_inferior.grid(row=2, column=2, padx=10, pady=10)

ventana.mainloop()
