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
# frame azul
#.....................................
frame_azul = Frame (ventana_principal)
frame_azul.config(bg="blue",width=167, height=250)
frame_azul.place(x=0, y=0)

#.....................................
# frame blanco
#.....................................
frame_blanco = Frame (ventana_principal)
frame_blanco.config(bg="white",width=167, height=250)
frame_blanco.place(x=167, y=0)

#.....................................
# frame rojo
#.....................................
frame_rojo = Frame (ventana_principal)
frame_rojo.config(bg="red",width=167, height=250)
frame_rojo.place(x=334, y=0)

# run

# se ejecuta el metodo mainloop()de la clase Tk() a traves de la instancia ventana_principal.Este boton despliega la ventana en pantalla y queda a la espera de lo que el usuario haga (clik en un boton,escribir,etc).Cada accion del usuario se conoce como un evento . El metodo mainloop()es un bucle infinito.

ventana_principal.mainloop()