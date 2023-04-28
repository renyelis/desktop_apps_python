#.....................................
# Desktop app No.1
#.....................................

# se importa la libreria tkinter con todas sus funciones 
from tkinter import *

#.....................................
# funciones de la app
#.....................................

#.....................................
# ventana principal de la app
#.....................................

# se declara una variable llamada ventana_principal, que adquiere las caracteristicas de un objeto Tk()
ventana_principal = Tk()

# titulo de la ventana
ventana_principal.title("Especialidad en sistemas-Guanenta")

# tamaño de la ventana
ventana_principal.geometry("500x250")

# desabilitar boton de maximizar
ventana_principal.resizable(False,False)

# color de fondo de la ventana
ventana_principal.config(bg="green")

#.....................................
# frame rojo
#.....................................
frame_rojo = Frame (ventana_principal)
frame_rojo.config(bg="red",width=500, height=62.5)
frame_rojo.place(x=0, y=0)

#.....................................
# frame amarillo
#.....................................
frame_amarillo = Frame (ventana_principal)
frame_amarillo.config(bg="yellow",width=500, height=125)
frame_amarillo.place(x=0, y=62.5)

#.....................................
# frame rojo
#.....................................
frame_rojo1 = Frame (ventana_principal)
frame_rojo1.config(bg="red",width=500, height=62.5)
frame_rojo1.place(x=0, y=187.5)

#.....................................
# frame cuadrado
#.....................................
frame_cuadrado = Frame (ventana_principal)
frame_cuadrado.config(bg="black",width=100, height=100)
frame_cuadrado.place(x=50, y=75)

# run

# se ejecuta el metodo mainloop()de la clase Tk() a traves de la instancia ventana_principal.Este boton despliega la ventana en pantalla y queda a la espera de lo que el usuario haga (clik en un boton,escribir,etc).Cada accion del usuario se conoce como un evento . El metodo mainloop()es un bucle infinito.

ventana_principal.mainloop()