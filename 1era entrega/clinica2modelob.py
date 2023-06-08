from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3

#Diseño de la ventana
ventana = Tk()                              #Con esta linea creamos la ventana del programa
ventana.title('GRUD')                       #COn .title() le agregamos un titulo a la ventana
ventana.geometry('600x350')                 #Con .geometry() agregamos las dimensiones de la ventana


#Campos
miID=StringVar()
miNombre=StringVar()
miCargo=StringVar()
miSalario=StringVar()


#Funcion para crear/conectar con la base de datos
def conexionBBDD():
    conexion=sqlite3.connect('base')
    cursor=conexion.cursor()
    try:
        cursor.execute('''
                       CREATE TABLE Empleados (
                           ID INTEGER PRIMARY KEY AUTOINCREMENT,
                           Nombre VARCHAR(50) NOT NULL,
                           Cargo VARCHAR(50) NOT NULL,
                           Salario INT NOT NULL)
                       ''')
        messagebox.showinfo('CONEXION','Base de datos creada existosamente')
    except:
        messagebox.showinfo('CONEXION','Se conecto existosamente con la base de datos')
   

#Funcion para eliminar la base de datos en caso de ser necesario       
def eliminarBBDD():
    conexion=sqlite3.connect('base')
    cursor=conexion.cursor()
    if messagebox.askyesno(message='Los datos se perderan definitivamente, desea continuar?',title='ADVERTENCIA'):
        cursor.execute('DROP TABLE Empleados')
    

#Funcion para limpiar un campo en caso de ser necesario
def limpiarCampos():
    miID.set('')
    miNombre.set('')
    miCargo.set('')
    miSalario.set('')

    
#Funcion que muestra informacion de la aplicacion
def acercaDe():
    informacion='''
    Aplicacion CRUD
    Version 1.0
    Desarrollado en Python
    Santi
    Tqm
    '''
    messagebox.showinfo(title='INFORMACION',message=informacion)
    
 
#Tabla
tabla=ttk.Treeview(height=10,columns=('#0','#1','#2'))     #Con esta funcion creamos una tabla con columnas en horizontal
tabla.place(x=0,y=130)
tabla.column('#0',width=100)
tabla.heading('#0',text='ID',anchor=CENTER)
tabla.heading('#1',text='Nombre del empleado',anchor=CENTER)
tabla.heading('#2',text='Cargo',anchor=CENTER)
tabla.column('#3', width=100)
tabla.heading('#3',text='Salario',anchor=CENTER)    


#Seleccionar usando click
def seleccionarConClick(event):
    item=tabla.identify('item',event.x,event.y)
    miID.set(tabla.item(item,'text'))
    miNombre.set(tabla.item(item,"values")[0])
    miCargo.set(tabla.item(item,"values")[1])
    miSalario.set(tabla.item(item,"values")[2])

tabla.bind("<Button-1>", seleccionarConClick)
   
#Funcion para salir de la aplicacion
def salir():
    valor=messagebox.askquestion('SALIR','Estas seguro que deseas salir de la aplicacion?')
    if valor=='yes':
        ventana.destroy()
        

######################################## METODOS CRUD ########################################


#Create
def crear():
    conexion=sqlite3.connect('base')
    cursor=conexion.cursor()
    try:
        datos=miNombre.get(),miCargo.get(),miSalario.get()
        cursor.execute('INSERT INTO Empleados VALUES(NULL,?,?,?)',(datos))
        conexion.commit()
    except:
        messagebox.showwarning('ADVERTENCIA','Ocurrio un error al crear el registro')
        pass
    limpiarCampos()
    mostrar()


#Read
def mostrar():
    conexion=sqlite3.connect('base')
    cursor=conexion.cursor()
    registros=tabla.get_children()
    for elemento in registros:
        tabla.delete(elemento)
    try:
        cursor.execute('SELECT * FROM Empleados')
        for row in cursor:
            tabla.insert('',0,text=row[0],values=(row[1],row[2],row[3]))
    except:
        pass


#Update
def actualizar():
    conexion = sqlite3.connect("base")
    cursor = conexion.cursor()
    try:
        datos = miNombre.get(), miCargo.get(), miSalario.get(), miID.get()
        cursor.execute('UPDATE Empleados SET Nombre=?, Cargo=?, Salario=? WHERE ID=?', datos)
        conexion.commit()
        messagebox.showinfo('REGISTRO', 'Registro actualizado exitosamente')
    except:
        messagebox.showwarning("ADVERTENCIA", "Ocurrió un error al actualizar el registro")
    finally:
        conexion.close()
    limpiarCampos()
    mostrar()

#Delete
def borrar():
    conexion=sqlite3.connect('base')
    cursor=conexion.cursor()
    try:
        if messagebox.askyesno(message='Realmente quiere borrar el registro?',title='ADVERTENCIA'):
            cursor.execute('DELETE FROM Empleados WHERE ID='+miID.get())
            conexion.commit()
    except:
        messagebox.showwarning('ADVERENCIA','Ocurrio un error al tratar de eliminar el registro')
    limpiarCampos()
    mostrar()


#Barra de menu
menubar=Menu(ventana)                                                                     #Con menu() colocamos una barra de menu en nuestra ventana

menubasedat=Menu(menubar,tearoff=0)                                                       #
menubasedat.add_command(label='Crear/Conectar Base de Datos',command=conexionBBDD)        #
menubasedat.add_command(label='Eliminar Base de Datos',command=eliminarBBDD)              #
menubasedat.add_command(label='Salir',command=salir)                                      #
menubar.add_cascade(label='Inicio',menu=menubasedat)

ayudamenu=Menu(menubar,tearoff=0)
ayudamenu.add_command(label='Resetear Campos',command=limpiarCampos)                      #
ayudamenu.add_command(label='Acerca De',command=acercaDe)
menubar.add_cascade(label='Ayuda',menu=ayudamenu) 

ventana.config(menu=menubar)

#Formulario
e1=Entry(ventana,textvariable=miID)

l2=Label(ventana,text='Nombre')
l2.place(x=50,y=10)
e2=Entry(ventana,textvariable=miNombre, width=50)
e2.place(x=100,y=10)

l3=Label(ventana,text='Cargo')
l3.place(x=50,y=40)
e3=Entry(ventana,textvariable=miCargo)
e3.place(x=100,y=40)

l4=Label(ventana,text='Salario')
l4.place(x=275,y=40)
e4=Entry(ventana,textvariable=miSalario, width=10)
e4.place(x=315,y=40)

l5=Label(ventana,text="USD")
l5.place(x=375,y=40)


#Botones
b1=Button(ventana,text='Crear Registro',command=crear)
b1.place(x=50,y=90)

b1=Button(ventana,text='Modificar Registro',command=actualizar)
b1.place(x=170,y=90)

b1=Button(ventana,text='Mostrar Lista',command=mostrar)
b1.place(x=330,y=90)

b1=Button(ventana,text='Eliminar Registro',bg='red',command=borrar)
b1.place(x=450,y=90)

ventana.config(menu=menubar)
ventana.mainloop()              #ventana.mainloop() nos permite ejecutar la ventana