#Importaciones de librerias y módulos

import tkinter as tk #sudo apt-get install python3-tk en mac
from tkinter import ttk
from tkinter import messagebox
import sys


#Fin de las importaciones de librerias y módulos

#############################################################################

#Inicio de las funciones

def sumar():
    cajatres.delete(0, tk.END)
    a = caja.get()
    b = cajados.get()
    try:
        a = float(a)
        b = float(b)
        c = a + b
        cajatres.insert(0, c)
        caja.delete(0, tk.END)
        cajados.delete(0, tk.END)
    except ValueError:
        cajatres.insert(0, "Error")

def restar():
    cajatres.delete(0, tk.END)
    a = caja.get()
    b = cajados.get()
    try:
        a = float(a)
        b = float(b)
        c = a - b
        cajatres.insert(0, c)
        caja.delete(0, tk.END)
        cajados.delete(0, tk.END)
    except ValueError:
        cajatres.insert(0, "Error")

def multiplicar():
    cajatres.delete(0, tk.END)
    a = caja.get()
    b = cajados.get()
    try:
        a = float(a)
        b = float(b)
        c = a * b
        cajatres.insert(0, c)
        caja.delete(0, tk.END)
        cajados.delete(0, tk.END)
    except ValueError:
        cajatres.insert(0, "Error")

def dividir():
    cajatres.delete(0, tk.END)
    a = caja.get()
    b = cajados.get()
    try:
        a = float(a)
        b = float(b)
        c = a / b
        cajatres.insert(0, c)
        caja.delete(0, tk.END)
        cajados.delete(0, tk.END)
    except ValueError:
        cajatres.insert(0, "Error")
    except ZeroDivisionError:
        cajatres.insert(0, "Error por 0")

def info():
    messagebox.showinfo(title="Información", message="Calculadora Python")

def salir():
    if messagebox.askokcancel(title="Pregunta", message="¿Desea salir?"):
        sys.exit()

#Fin de las funciones

#############################################################################

#Inicio de la interfaz grafica

##Ventana##
ventana = tk.Tk()

ventana.title("Calculadora")

ventana.config(width=300, height=300)

##Botones##
botonsuma = tk.Button(text="+", command=sumar)
botonsuma.place(x=30, y=130)

botonresta = tk.Button(text="-", command=restar)
botonresta.place(x=100, y=130)

botonmultiplica = tk.Button(text="x", command=multiplicar)
botonmultiplica.place(x=170, y=130)

botondivide = tk.Button(text="/", command=dividir)
botondivide.place(x=240, y=130)

botoninfo = tk.Button(text="Info", command=info)
botoninfo.place(x=0, y=270)

botonsalir = tk.Button(text="Salir", command=salir)
botonsalir.place(x=250, y=270)

##Cajas de texto##
caja = tk.Entry()
caja.place(x=10, y=50)

cajados = tk.Entry()
cajados.place(x=165, y=50)

cajatres = tk.Entry()
cajatres.place(x=85, y=200)

##Textos##

datosuno = tk.Label(text="Primer dato:")
datosuno.place(x=10, y=20)

datosdos = tk.Label(text="Segundo dato:")
datosdos.place(x=165, y=20)

botonera = tk.Label(text=">>> Botonera <<<")
botonera.place(x=95, y=95)

resultados = tk.Label(text="Resultado:")
resultados.place(x=110, y=170)

##Mainloop##

ventana.mainloop()

#Fin de la interfaz grafica