#---------------------------------
# Desktop app No. 1
#---------------------------------

# se importa la libreria tkinter con todas sus funciones 
from tkinter import *
from tkinter import messagebox

#----------------------------
# funciones de la app
#----------------------------

#SUMAR
def sumar():
    pass
#BORRAR
def borra():
    pass
#SALIR
def salir():
    messagebox.showinfo("Suma Enteros 1.0","la app se va a cerrar")
    ventana_principal.destroy()
#-----------------------------
# ventana principal de la app
#-----------------------------

# se declara una variable llamada ventana_principal, que adquiere las caracteristicas de un objeto Tk()
ventana_principal = Tk()

# TAMAÑO DE LA VENTANA 
ventana_principal.geometry("500x500")

# TITULO DE VENTANA
ventana_principal.title("SUMA ENTEROS 1.0")

# DESHABILITAR BOTON DE MAXIMIZAR
ventana_principal.resizable(False, False)

# COLOR DE FONDO DE LA VENTANA 
ventana_principal.config(bg="purple3")

#-------------------------
# VARIABLES GLOBALES
#-------------------------
x = StringVar()
y = StringVar()

#-------------------------
# FRAMA ENTRADA DATOS
#-------------------------
frame_entrada = Frame(ventana_principal)
frame_entrada.config(bg="white", width=480, height=180)
frame_entrada.place(x=10, y=10)


# LOGO DE LA APP 
logo = PhotoImage(file="img/escudo_colegio.png")
lb_logo = Label(frame_entrada, image=logo, bg="white")
lb_logo.place(x=70,y=40)


# TITULO DE APP 
titulo = Label(frame_entrada, text="suma_enteros_1.0")
titulo.config(bg ="white", fg="purple3", font=("Helvetica", 20))
titulo.place(x=240,y=10)

# ETIQUETA PARA VALOR DE X
lb_x= Label(frame_entrada, text = "X = ")
lb_x.config(bg="white", fg="purple3", font=("Helvetica", 18))
lb_x.place(x=240,y=60)


# CAJA DE TEXTO PARA VALOR X
entry_x = Entry(frame_entrada, textvariable=x)
entry_x.config(bg="white", fg="purple3", font=("Times New Roman", 18), width=6)
entry_x.place(x=290,y=60)

# ETIQUETA PARA VALOR DE Y
lb_y= Label(frame_entrada, text = "Y = ")
lb_y.config(bg="white", fg="purple3", font=("Helvetica", 18))
lb_y.place(x=240,y=120)


# CAJA DE TEXTO PARA VALOR Y
entry_y = Entry(frame_entrada,textvariable=y)
entry_y.config(bg="white", fg="purple3", font=("Times New Roman", 18), width=6)
entry_y.place(x=290,y=120)


#-------------------------
# FRAMA OPERACIONES
#-------------------------
frame_operaciones = Frame(ventana_principal)
frame_operaciones.config(bg="white", width=480, height=100)
frame_operaciones.place(x=10, y=200)

# BOTON PARA SUMAR
bt_sumar=Button(frame_operaciones, text="Sumar",command=sumar)
bt_sumar.place(x=45 , y=35 , width=100,height=30)

# BOTON PARA BORRAR
bt_borrar=Button(frame_operaciones, text="Borrar",command=borra)
bt_borrar.place(x=190 , y=35 , width=100,height=30)

# BOTN PARA SALIR
bt_salir=Button(frame_operaciones, text="Salir", command=salir)
bt_salir.place(x=335, y=35 , width=100,height=30)

#-------------------------
# FRAMA RESULTADOS
#-------------------------
frame_resultados = Frame(ventana_principal)
frame_resultados.config(bg="white", width=480, height=180)
frame_resultados.place(x=10, y=310)

# AREA DE TEXTO PARA LOS RESULTADOS
t_resultados = Text(frame_resultados)
t_resultados.config(bg="black", fg="green yellow", font=("courier",20))
t_resultados.place(x=10,y=10,width=460,height=160)

# run 
# SE EJECUTA EL METODO MAINLOOP() DE LA CLASE TK() A TRAVES DE LA INSTANCIA DE LA INTANCIA ventana_principal. Este metodo despliega la ventana en pantalla y queda a la espera de le que el usuario haga (click en un boton, escribir, etc). Cada accion del usuario se conoce como unn evento. El método mainloop() es un bucle infinito.
ventana_principal.mainloop()




