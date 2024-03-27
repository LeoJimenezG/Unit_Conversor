from tkinter import *
from tkinter import messagebox


#Creación de la raíz
root=Tk()
root.title("Conversor de Unidades")
root.resizable(0,0)
root.iconbitmap("icono.ico")

#Creación del frame
frame=Frame(root)
frame.pack(fill="none", expand="False")
frame.configure(width=600, height=500, border=1, relief="solid", background="#F2EEE3")
frame.grid_propagate(False)
frame.pack_propagate(False)

#Creación del contenido de inicio
imagen=PhotoImage(file="CDU_logo.png")
imagen=imagen.subsample(x=2,y=2)
logoImagen=Label(frame, image=imagen)
logoImagen.pack(pady=80)

#Creación de variables globales a usar
unidadConv=StringVar()
resultadoConv=StringVar()
tituloConv=StringVar()
codigosConv={1:"Gramos a Kilogramos", 2:"Gramos a Libras", 3:"Kilogramos a Gramos", 4:"Kilogramos a Libras", 5:"Libras a Gramos", 6:"Libras a Kilogramos", 7:"Centímetros a Metros", 8:"Centímetros a Kilómetros", 
            9:"Metros a Centímetros", 10:"Metros a Kilómetros", 11:"Kilómetros a Centímetros", 12:"Kilómetros a Metros", 13:"Segundos a Minutos", 14:"Segundos a Horas", 15:"Minutos a Segundos", 16:"Minutos a Horas",
            17:"Horas a Segundos", 18:"Horas a Minutos", 19:"Celcuis a Fahrenheit", 20:"Celcius a Kelvin", 21:"Fahrenheit a Celcius", 22:"Fahrenheit a Kelvin", 23:"Kelvin a Celcius", 24:"Kelvin a Fahrenheit"}
opcionAct=0
tipoConv=0

#Funciones de las herramientas
def tipoConversion(num):
    global tipoConv
    tipoConv=num
    tituloConv.set('"'+codigosConv[tipoConv]+'"')
    mostrarElementos()

def mostrarElementos():
    global descripcion, opcionAct
    logoImagen.destroy()
    opcionAct+=1
    if(opcionAct<2):
        Label(frame,text="", background="#F2EEE3", font=("", 1)).pack()
        titulo=Label(frame,textvariable=tituloConv, font=("Bahnschrift", 20, "bold", "underline", "italic"), background="#F2EEE3")
        titulo.pack()
        Label(frame,text="").pack()
        unidad=Label(frame, text="Cantidad a Convertir", font=("Bahnschrift", 18),background="#F2EEE3")
        unidad.pack()
        unidad.configure(justify="center")
        unidadConvertir=Entry(frame, textvariable=unidadConv, font=("Comic Sans MS", 14))
        unidadConvertir.pack()
        unidadConvertir.configure(justify="left")
        Label(frame,text="", background="#F2EEE3").pack()
        conversion=Label(frame, text="Resultado", font=("Bahnschrift", 18), background="#F2EEE3")
        conversion.pack()
        conversion.configure(justify="center")
        unidadConvertida=Entry(frame, textvariable=resultadoConv, font=("Comic Sans MS", 14))
        unidadConvertida.pack()
        unidadConvertida.configure(justify="left")
        obtenerRes=Button(frame, text="Convertir", command=obtenerResultado, font=("Bahnschrift", 14), activebackground="#6879B1", background="#F2EEE3", width=8, height=1, padx=2)
        obtenerRes.place(x=190, y=280)
        borrarEntrada=Button(frame, text="Borrar", command=borrarPantalla, font=("Bahnschrift", 14), activebackground="#6879B1", background="#F2EEE3", width=8, height=1, padx=2)
        borrarEntrada.place(x=310, y=280)
    else:
        unidadConv.set("")
        resultadoConv.set("")
    
def obtenerResultado():
    global unidadConv, resultadoConv, tipoConv
    resultado=0
    match tipoConv:
        case 1:
            resultado=float(unidadConv.get())/1000
        case 2:
            resultado=float(unidadConv.get())/453.5924
        case 3:
            resultado=float(unidadConv.get())*1000
        case 4:
            resultado=float(unidadConv.get())*2.204623
        case 5:
            resultado=float(unidadConv.get())*453.5924
        case 6:
            resultado=float(unidadConv.get())/2.204623
        case 7:
            resultado=float(unidadConv.get())/100
        case 8:
            resultado=float(unidadConv.get())/100000
        case 9:
            resultado=float(unidadConv.get())*100
        case 10:
            resultado=float(unidadConv.get())/1000
        case 11:
            resultado=float(unidadConv.get())*100000
        case 12:
            resultado=float(unidadConv.get())*1000
        case 13:
            resultado=float(unidadConv.get())/60
        case 14:
            resultado=float(unidadConv.get())/3600
        case 15:
            resultado=float(unidadConv.get())*60
        case 16:
            resultado=float(unidadConv.get())/60
        case 17:
            resultado=float(unidadConv.get())*3600
        case 18:
            resultado=float(unidadConv.get())*60
        case 19:
            resultado=float(unidadConv.get())*1.8+32
        case 20:
            resultado=float(unidadConv.get())+273.15
        case 21:
            resultado=(float(unidadConv.get())-32)/1.8
        case 22:
            resultado=((5*(float(unidadConv.get())-32))/9)+273.15
        case 23:
            resultado=float(unidadConv.get())-273.15
        case 24:
            resultado=((9*(float(unidadConv.get())-273.15))/5)+32
    resultadoConv.set(str(resultado))

def borrarPantalla():
    global unidadConv, resultadoConv
    unidadConv.set("")
    resultadoConv.set("")
 
def calculadora():
    
    pass

def sobrePrograma():
    messagebox.showinfo("Sobre el Programa", "Conversor de Unidades es un programa creado con la intención de facilitar el proceso de conversión de unidades. Es un proyecto básico y sencillo.")
    
def sobreDesarrollador():
    messagebox.showinfo("Sobre el Desarrollador", "Soy Leonardo Jiménez González, estudiante de Ingeniería de Software. Trabajo en proyectos académicos y personales.")

#Creación de la barra de menus
barraMenu=Menu(root)
root.config(menu=barraMenu)

masaMenu=Menu(barraMenu, tearoff=0)
longitudMenu=Menu(barraMenu, tearoff=0)
tiempoMenu=Menu(barraMenu, tearoff=0)
temperaturaMenu=Menu(barraMenu, tearoff=0)
#calculadoraMenu=Menu(barraMenu, tearoff=0)
masMenu=Menu(barraMenu, tearoff=0)

masaMenu.add_command(label="Gramo a Kilogramo", command=lambda:tipoConversion(1))
masaMenu.add_command(label="Gramo a Libra", command=lambda:tipoConversion(2))
masaMenu.add_command(label="Kilogramo a Gramo", command=lambda:tipoConversion(3))
masaMenu.add_command(label="Kilogramo a Libra", command=lambda:tipoConversion(4))
masaMenu.add_command(label="Libra a Gramo", command=lambda:tipoConversion(5))
masaMenu.add_command(label="Libra a Kilogramo", command=lambda:tipoConversion(6))

longitudMenu.add_command(label="Centímetro a Metro", command=lambda:tipoConversion(7))
longitudMenu.add_command(label="Centímetro a Kilómetro", command=lambda:tipoConversion(8))
longitudMenu.add_command(label="Metro a Centímetro", command=lambda:tipoConversion(9))
longitudMenu.add_command(label="Metro a Kilómetro", command=lambda:tipoConversion(10))
longitudMenu.add_command(label="Kilómetro a Centímetro", command=lambda:tipoConversion(11))
longitudMenu.add_command(label="Kilómetro a Metro", command=lambda:tipoConversion(12))

tiempoMenu.add_command(label="Segundo a Minuto", command=lambda:tipoConversion(13))
tiempoMenu.add_command(label="Segundo a Hora", command=lambda:tipoConversion(14))
tiempoMenu.add_command(label="Minuto a Segundo", command=lambda:tipoConversion(15))
tiempoMenu.add_command(label="Minuto a Hora", command=lambda:tipoConversion(16))
tiempoMenu.add_command(label="Hora a Segundo", command=lambda:tipoConversion(17))
tiempoMenu.add_command(label="Hora a Minuto", command=lambda:tipoConversion(18))

temperaturaMenu.add_command(label="Celcius a Fahrenheit", command=lambda:tipoConversion(19))
temperaturaMenu.add_command(label="Celcius a Kelvin", command=lambda:tipoConversion(20))
temperaturaMenu.add_command(label="Fahrenheit a Celcius", command=lambda:tipoConversion(21))
temperaturaMenu.add_command(label="Fahrenheit a Kelvin", command=lambda:tipoConversion(22))
temperaturaMenu.add_command(label="Kelvin a Celcius", command=lambda:tipoConversion(23))
temperaturaMenu.add_command(label="Kelvin a Fahrenheit", command=lambda:tipoConversion(24))

masMenu.add_command(label="Sobre el programa", command=lambda:sobrePrograma())
masMenu.add_command(label="Sobre el desarrollador", command=lambda:sobreDesarrollador())

barraMenu.add_cascade(label="Masa", menu=masaMenu)
barraMenu.add_cascade(label="Longitud", menu=longitudMenu)
barraMenu.add_cascade(label="Tiempo", menu=tiempoMenu)
barraMenu.add_cascade(label="Temperatura", menu=temperaturaMenu)
barraMenu.add_cascade(label="Más", menu=masMenu)

root.mainloop()