from Tkinter import *
import sys, os

ventana0 = Tk()
ventana1 = Toplevel(ventana0)

def mostrar(ventana) :
	ventana.deiconify()
def ocultar(ventana) :
	ventana.withdraw()
def ejecutar(f) :
	ventana0.after(200,f)


ventana0.config(bg="black")
ventana0.geometry("600x600")

b1 = Button(ventana0,text="Abrir",command=lambda: ejecutar(mostrar(ventana1)))
b1.grid(row=1,column=1)
b2 = Button(ventana0,text="Ocultar",command=lambda: ejecutar(ocultar(ventana1)))
b2.grid(row=1,column=2)


ventana1.withdraw()
ventana0.mainloop()

