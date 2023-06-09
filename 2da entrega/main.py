from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import os
import mysql.connector

# Crear la ventana principal
ventana = Tk()
ventana.title("Gestión de Hospital")
ventana.geometry("1456x670")

carpetaDeTodosLosArchivos = os.path.dirname(__file__)
carpetaLogo = os.path.join(carpetaDeTodosLosArchivos, 'Iconos')
image_path = os.path.join(carpetaLogo, 'perropepsi.ico')
ventana.iconbitmap(image_path)


# Crear el Notebook
notebook = ttk.Notebook(ventana)

# Crear las pestañas
ventana1 = ttk.Frame(notebook)
ventana2 = ttk.Frame(notebook)
ventana3 = ttk.Frame(notebook)
ventana4 = ttk.Frame(notebook)

ventana1.pack(fill='both', expand=1)
ventana2.pack(fill='both', expand=1)
ventana3.pack(fill='both', expand=1)
ventana4.pack(fill='both', expand=1)

notebook.add(ventana1, text='Paciente')
notebook.add(ventana2, text='Medicos')
notebook.add(ventana3, text='Busqueda Pacientes')
notebook.add(ventana4, text='Busqueda Medicos')

# Agregar el Notebook a la ventana
notebook.pack(fill="both", expand=True)


#Agrega el desplegable
genero_combobox = ttk.Combobox(ventana1, values=["Masculino", "Femenino", "Otro"])
genero_combobox.place(x=10, y=192)


#Declara el valor a las variables
id = StringVar()
nombre = StringVar()
apellido = StringVar()
fecha_nacimiento = StringVar()
celular = StringVar()
cuit = StringVar()
correo_electronico = StringVar()
barrio = StringVar()
calle = StringVar()
numero_calle = StringVar()
pais = StringVar()
provincia = StringVar()


#Funcion que muestra informacion de la aplicacion
def acercaDe():
    informacion='''
    Aplicacion CRUD
    Version 2.0
    Desarrollado en Python
    '''
    messagebox.showinfo(title='INFORMACION',message=informacion)


#Funcion para limpiar un campo en caso de ser necesario
def limpiarCampos():
    nombre.set('')
    apellido.set('')
    fecha_nacimiento.set('')
    celular.set('')
    cuit.set('')
    correo_electronico.set('')
    barrio.set('')
    calle.set('')
    numero_calle.set('')
    pais.set('')
    provincia.set('')


#Tabla
tabla=ttk.Treeview(ventana1, height=15, columns=('#0','#1','#2','#3','#4','#5','#6','#7','#8','#9','#10','#11','#12'))
tabla.place(x=10,y=230)

columnas = ['ID','Nombre', 'Apellido', 'Fecha Nacimiento', 'Género', 'CUIT', 'Celular', 'Correo Electrónico', 'Barrio', 'Calle', 'N° de Calle', 'País', 'Provincia']
tabla["columns"] = columnas
tabla["show"] = "headings"
for columna in columnas:
    tabla.column(columna, width=110)
    tabla.heading(columna, text=columna)

#Seleccionar usando click
def seleccionarConClick(event):
    item = tabla.identify('item', event.x, event.y)
    values = tabla.item(item, 'values')
    id.set(values[0])
    nombre.set(values[1])
    apellido.set(values[2])
    fecha_nacimiento.set(values[3])
    genero_combobox.set(values[4])
    cuit.set(values[5])
    celular.set(values[6])
    correo_electronico.set(values[7])
    barrio.set(values[8])
    calle.set(values[9])
    numero_calle.set(values[10])
    pais.set(values[11])
    provincia.set(values[12])


tabla.bind("<Button-1>", seleccionarConClick)


#CRUD C = Create R = Read U = Update D = Delete 

# Read
def mostrar():
    conexion = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='sistemaclinicafinalparaprogramacion'
    )
    cursor = conexion.cursor()    
    registros = tabla.get_children()
    for elemento in registros:
        tabla.delete(elemento)
    try:
        cursor.execute('SELECT * FROM pacientes')
        for row in cursor:
            tabla.insert('', 0, text=row[0], values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12]))
    except mysql.connector.Error:
        pass
    finally:
        cursor.close()
        conexion.close()


# Create
def agregar_paciente():
    conexion = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='sistemaclinicafinalparaprogramacion'
    )
    cursor = conexion.cursor()
    try:
        datos = (
            #Con el .get agarramos los datos ingresados por el usuario
            nombre.get(),
            apellido.get(),
            fecha_nacimiento.get(),
            genero_combobox.get(),
            cuit.get(),
            celular.get(),
            correo_electronico.get(),
            barrio.get(),
            calle.get(),
            numero_calle.get(),
            pais.get(),
            provincia.get()
        )
        cursor.execute(
            'INSERT INTO pacientes (nombre, apellido, fechaNacimiento, genero, cuit, telefonoCelular, correoElectronico, barrio, calle, numero, pais, provincia) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', datos)
        conexion.commit()
        messagebox.showinfo('INFO','Paciente agregado correctamente')
    except mysql.connector.Error as error:
        messagebox.showwarning('ADVERTENCIA', 'Ocurrió un error al agregar el paciente')
    finally:
        cursor.close()
        conexion.close()
    limpiarCampos()
    mostrar()
    

def modificar_paciente():
    conexion = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='sistemaclinicafinalparaprogramacion'
    )
    cursor = conexion.cursor()
    try:
        datos = (
        nombre.get(),
        apellido.get(),
        fecha_nacimiento.get(),
        genero_combobox.get(),
        cuit.get(),
        celular.get(),
        correo_electronico.get(),
        barrio.get(),
        calle.get(),
        numero_calle.get(),
        pais.get(),
        provincia.get(),
        id.get())
        cursor.execute('UPDATE pacientes SET nombre=%s, apellido=%s, fechaNacimiento=%s, genero=%s, cuit=%s, telefonoCelular=%s, correoElectronico=%s, barrio=%s, calle=%s, numero=%s, pais=%s, provincia=%s WHERE IDPacientes=%s', datos)
        conexion.commit()
        messagebox.showinfo('REGISTRO', 'Registro actualizado exitosamente')
    except:
        messagebox.showwarning("ADVERTENCIA", "Ocurrió un error al actualizar el registro")
    finally:
        conexion.close()
    limpiarCampos()
    mostrar()


def eliminar_paciente():
    conexion = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='sistemaclinicafinalparaprogramacion'
    )
    cursor = conexion.cursor()
    try:
        if messagebox.askyesno(message='¿Realmente quiere borrar el registro?', title='ADVERTENCIA'):
            cursor.execute('DELETE FROM pacientes WHERE IDPacientes=%s', (id.get(),))
            conexion.commit()
            messagebox.showinfo('INFO', 'El registro se eliminó correctamente')
    except mysql.connector.Error as error:
        messagebox.showwarning('ADVERTENCIA', 'Ocurrió un error al tratar de eliminar el registro')
    finally:
        cursor.close()
        conexion.close()
    limpiarCampos()
    mostrar()


#Barra de menu
menubar=Menu(ventana)

ayudamenu=Menu(menubar,tearoff=0)
ayudamenu.add_command(label='Resetear Campos',command=limpiarCampos)                      
ayudamenu.add_command(label='Acerca De',command=acercaDe)
menubar.add_cascade(label='Ayuda',menu=ayudamenu) 
ventana.config(menu=menubar)

# Etiquetas
label_ID = ttk.Label(ventana1, text="ID:")
label_ID.place (x=10, y=10)

label_nombre = ttk.Label(ventana1, text="Nombre:")
label_nombre.place (x=10, y=50)

label_apellido = ttk.Label(ventana1, text="Apellido:")
label_apellido.place (x=10, y=90)

label_fecha_nacimiento = ttk.Label(ventana1, text="Fecha de Nacimiento:")
label_fecha_nacimiento.place (x=10, y=130)

label_genero = ttk.Label(ventana1, text="Género:")
label_genero.place (x=10, y=170)

label_cuit = ttk.Label(ventana1, text="CUIT:")
label_cuit.place (x=350, y=50)

label_celular = ttk.Label(ventana1, text="Celular:")
label_celular.place (x=350, y=90)

label_correo_electronico = ttk.Label(ventana1, text="Correo Electrónico:")
label_correo_electronico.place (x=350, y=130)

label_barrio =ttk.Label(ventana1, text="Barrio:")
label_barrio.place (x=350, y=170)

label_calle = ttk.Label(ventana1, text="Calle:")
label_calle.place (x=700, y=50)

label_n_calle = ttk.Label(ventana1, text="Número de Calle:")
label_n_calle.place (x=700, y=90)

label_pais = ttk.Label(ventana1, text="País:")
label_pais.place (x=700, y=130)

label_provincia = ttk.Label(ventana1, text="Provincia:")
label_provincia.place (x=700, y=170)


# Campos de entrada
entry_ID = ttk.Entry(ventana1, textvariable=id, state='disabled')
entry_ID.place (x=10, y=30)

entry_nombre = ttk.Entry(ventana1,textvariable=nombre)
entry_nombre.place (x=10, y=70)

entry_apellido = ttk.Entry(ventana1,textvariable=apellido)
entry_apellido.place (x=10, y=110)

entry_fecha_nacimiento = ttk.Entry(ventana1,textvariable=fecha_nacimiento)
entry_fecha_nacimiento.place (x=10, y=150)

entry_cuit = ttk.Entry(ventana1,textvariable=cuit)
entry_cuit.place (x=350, y=70)

entry_celular = ttk.Entry(ventana1,textvariable=celular)
entry_celular.place (x=350, y=110)

entry_correo_electronico = ttk.Entry(ventana1,textvariable=correo_electronico)
entry_correo_electronico.place (x=350, y=150)

entry_barrio = ttk.Entry(ventana1,textvariable=barrio)
entry_barrio.place (x=350, y=190)

entry_calle = ttk.Entry(ventana1,textvariable=calle)
entry_calle.place (x=700, y=70)

entry_n_calle = ttk.Entry(ventana1,textvariable=numero_calle)
entry_n_calle.place (x=700, y=110)

entry_pais = ttk.Entry(ventana1,textvariable=pais)
entry_pais.place (x=700, y=150)

entry_provincia = ttk.Entry(ventana1,textvariable=provincia)
entry_provincia.place (x=700, y=190)

# Botones
btn_agregar = ttk.Button(ventana1,  text="Agregar", command=agregar_paciente)
btn_agregar.place (x=15, y=580)

btn_modificar = ttk.Button(ventana1, text="Modificar", command=modificar_paciente)
btn_modificar.place (x=105, y=580)

btn_eliminar = ttk.Button(ventana1, text="Eliminar", command=eliminar_paciente)
btn_eliminar.place (x=195, y=580)

btn_salir = ttk.Button(ventana1, text="Listar", command=mostrar)
btn_salir.place (x=285, y=580)

btn_salir = ttk.Button(ventana1, text="Salir", command=ventana.quit)
btn_salir.place (x=375, y=580)


#_________________________________DOCTORES__________________________________________#

combo_especialidad_doctores = ttk.Combobox(ventana2, values=["Cardiólogo","Gastroentrólogo","Neumonólogo","Neurólogo","Pediatra","Trumatólogo","Endocrinólogo","Oncólogo","Radiólogo"])
combo_especialidad_doctores.place(x=1050,y=75)

genero_combobox_doctores = ttk.Combobox(ventana2, values=["Masculino", "Femenino", "Otro"])
genero_combobox_doctores.place (x=10, y=195)

id_doctores = StringVar()
nombre_doctores = StringVar()
apellido_doctores = StringVar()
fecha_nacimiento_doctores = StringVar()
celular_doctores = StringVar()
cuit_doctores = StringVar()
correo_electronico_doctores =  StringVar()
barrio_doctores = StringVar()
calle_doctores = StringVar()
numero_calle_doctores = StringVar()
pais_doctores = StringVar()
provincia_doctores = StringVar()

tabla2=ttk.Treeview(ventana2, height=15, columns=('#0','#1','#2','#3','#4','#5','#6','#7','#8','#9','#10','#11','#12','#13'))

tabla2.place(x=10,y=230)
columnas = ['ID','Nombre', 'Apellido', 'Fecha Nacimiento', 'Género', 'CUIT', 'Celular', 'Correo Electrónico', 'Barrio', 'Calle', 'N° de Calle', 'País', 'Provincia', "Especialidades"]
tabla2["columns"] = columnas
tabla2["show"] = "headings"
for columna in columnas:
    tabla2.column(columna, width=100)
    tabla2.heading(columna, text=columna)


#Seleccionar usando click
def seleccionarConClick(event):
    item2 = tabla2.identify('item', event.x, event.y)
    values = tabla2.item(item2, 'values')
    id_doctores.set(values[0])
    nombre_doctores.set(values[1])
    apellido_doctores.set(values[2])
    fecha_nacimiento_doctores.set(values[3])
    genero_combobox_doctores.set(values[4])
    cuit_doctores.set(values[5])
    celular_doctores.set(values[6])
    correo_electronico_doctores.set(values[7])
    barrio_doctores.set(values[8])
    calle_doctores.set(values[9])
    numero_calle_doctores.set(values[10])
    pais_doctores.set(values[11])
    provincia_doctores.set(values[12])
    combo_especialidad_doctores.set(values[13])
 

tabla2.bind("<Button-1>", seleccionarConClick)


# Read
def mostrar_doctores():
    conexion = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='sistemaclinicafinalparaprogramacion'
    )
    cursor = conexion.cursor()    
    registros2 = tabla2.get_children()
    for elemento2 in registros2:
        tabla2.delete(elemento2)
    try:
        cursor.execute('SELECT * FROM medicos')
        for row in cursor:
            tabla2.insert('', 0, text=row[0], values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13]))
    except mysql.connector.Error:
        pass
    finally:
        cursor.close()
        conexion.close()

#Create
def agregar_doctores():
    conexion = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='sistemaclinicafinalparaprogramacion'
    )
    cursor = conexion.cursor()
    try:
        datos2 = (
        nombre_doctores.get(), 
        apellido_doctores.get(), 
        fecha_nacimiento_doctores.get(), 
        genero_combobox_doctores.get(),
        cuit_doctores.get(),
        celular_doctores.get(),
        correo_electronico_doctores.get(),
        barrio_doctores.get(),
        calle_doctores.get(),
        numero_calle_doctores.get(),
        pais_doctores.get(),
        provincia_doctores.get(),
        combo_especialidad_doctores.get()) 
        cursor.execute('INSERT INTO medicos (nombre, apellido, fechaNacimiento, genero, cuit, telefonoCelular, correoElectronico, barrio, calle, numero, pais, provincia, especialidad) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', datos2)
        conexion.commit()
        messagebox.showinfo('INFO','Medico agregado correctamente')
    except mysql.connector.Error as error:
        messagebox.showwarning('ADVERTENCIA', 'Ocurrió un error al agregar el medico')
    finally:
        cursor.close()
        conexion.close()
    limpiarCampos()
    mostrar_doctores()

    

def modificar_doctores():
    conexion = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='sistemaclinicafinalparaprogramacion'
    )
    cursor = conexion.cursor()
    try:
        datos2 = (
            nombre_doctores.get(),
            apellido_doctores.get(),
            fecha_nacimiento_doctores.get(),
            genero_combobox_doctores.get(),
            cuit_doctores.get(),
            celular_doctores.get(),
            correo_electronico_doctores.get(),
            barrio_doctores.get(),
            calle_doctores.get(),
            numero_calle_doctores.get(),
            pais_doctores.get(),
            provincia_doctores.get(),
            combo_especialidad_doctores.get(),
            id_doctores.get()
        )
        cursor.execute('UPDATE medicos SET nombre=%s, apellido=%s, fechaNacimiento=%s, genero=%s, cuit=%s, telefonoCelular=%s, correoElectronico=%s, barrio=%s, calle=%s, numero=%s, pais=%s, provincia=%s, especialidad=%s WHERE IDMedicos=%s', datos2)
        conexion.commit()
        messagebox.showinfo('REGISTRO', 'Registro actualizado exitosamente')
    except:
        messagebox.showwarning("ADVERTENCIA", "Ocurrió un error al actualizar el registro")
    finally:
        cursor.close()
        conexion.close()
    limpiarCampos()
    mostrar_doctores()


def eliminar_doctores():
    conexion = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='sistemaclinicafinalparaprogramacion'
    )
    cursor = conexion.cursor()
    try:
        if messagebox.askyesno(message='¿Realmente quiere borrar el registro?', title='ADVERTENCIA'):
            cursor.execute('DELETE FROM medicos WHERE IDMedicos=%s', (id_doctores.get(),))
            conexion.commit()
            messagebox.showinfo('BORRAR', 'El registro se eliminó correctamente')
    except mysql.connector.Error as error:
        messagebox.showwarning('ADVERTENCIA', 'Ocurrió un error al tratar de eliminar el registro')
    finally:
        cursor.close()
        conexion.close()
    limpiarCampos()
    mostrar_doctores()



# Etiquetas
label_ID_doctores = ttk.Label(ventana2, text="ID:")
label_ID_doctores.place (x=10, y=10)

label_especialidad_doctores = ttk.Label(ventana2, text="Especialidad:")
label_especialidad_doctores.place (x=10, y=30)

label_nombre_doctores = ttk.Label(ventana2, text="Nombre:")
label_nombre_doctores.place (x=10, y=50)

label_apellido_doctores = ttk.Label(ventana2, text="Apellido:")
label_apellido_doctores.place (x=10, y=90)

label_fecha_nacimiento_doctores = ttk.Label(ventana2, text="Fecha de Nacimiento:")
label_fecha_nacimiento_doctores.place (x=10, y=130)

label_genero_doctores = ttk.Label(ventana2, text="Género:")
label_genero_doctores.place (x=10, y=170)

label_cuit_doctores = ttk.Label(ventana2, text="CUIT:")
label_cuit_doctores.place (x=350, y=50)

label_celular_doctores = ttk.Label(ventana2, text="Celular:")
label_celular_doctores.place (x=350, y=90)

label_correo_electronico_doctores = ttk.Label(ventana2, text="Correo Electrónico:")
label_correo_electronico_doctores.place (x=350, y=130)

label_barrio_doctores =ttk.Label(ventana2, text="Barrio:")
label_barrio_doctores.place (x=350, y=170)

label_calle_doctores = ttk.Label(ventana2, text="Calle:")
label_calle_doctores.place (x=700, y=50)

label_n_calle_doctores = ttk.Label(ventana2, text="Número de Calle:")
label_n_calle_doctores.place (x=700, y=90)

label_pais_doctores = ttk.Label(ventana2, text="País:")
label_pais_doctores.place (x=700, y=130)

label_provincia_doctores = ttk.Label(ventana2, text="Provincia:")
label_provincia_doctores.place (x=700, y=170)

label_especialidades_doctores = ttk.Label(ventana2, text="Especialidad:")
label_especialidades_doctores.place (x=1050, y=50)


# Campos de entrada Doctores
entry_ID_doctores= ttk.Entry (ventana2, textvariable=id_doctores, state='disabled')
entry_ID_doctores.place (x=10, y=30)

entry_nombre_doctores = ttk.Entry(ventana2,textvariable=nombre_doctores)
entry_nombre_doctores.place (x=10, y=70)

entry_apellido_doctores = ttk.Entry(ventana2,textvariable=apellido_doctores)
entry_apellido_doctores.place (x=10, y=110)

entry_fecha_nacimiento_doctores = ttk.Entry(ventana2,textvariable=fecha_nacimiento_doctores)
entry_fecha_nacimiento_doctores.place (x=10, y=150)

entry_cuit_doctores = ttk.Entry(ventana2,textvariable=cuit_doctores)
entry_cuit_doctores.place (x=350, y=70)

entry_celular_doctores = ttk.Entry(ventana2,textvariable=celular_doctores)
entry_celular_doctores.place (x=350, y=110)

entry_correo_electronico_doctores = ttk.Entry(ventana2,textvariable=correo_electronico_doctores)
entry_correo_electronico_doctores.place (x=350, y=150)

entry_barrio_doctores = ttk.Entry(ventana2,textvariable=barrio_doctores)
entry_barrio_doctores.place (x=350, y=190)

entry_calle_doctores = ttk.Entry(ventana2,textvariable=calle_doctores)
entry_calle_doctores.place (x=700, y=70)

entry_n_calle_doctores = ttk.Entry(ventana2,textvariable=numero_calle_doctores)
entry_n_calle_doctores.place (x=700, y=110)

entry_pais_doctores = ttk.Entry(ventana2,textvariable=pais_doctores)
entry_pais_doctores.place (x=700, y=150)

entry_provincia_doctores = ttk.Entry(ventana2,textvariable=provincia_doctores)
entry_provincia_doctores.place (x=700, y=190)


# Botones
btn_agregar_doctores = ttk.Button(ventana2,  text="Agregar", command=agregar_doctores)
btn_agregar_doctores.place (x=15, y=580)

btn_modificar_doctores = ttk.Button(ventana2, text="Modificar", command=modificar_doctores)
btn_modificar_doctores.place (x=105, y=580)

btn_eliminar_doctores = ttk.Button(ventana2, text="Eliminar", command=eliminar_doctores)
btn_eliminar_doctores.place (x=195, y=580)

btn_salir_doctores = ttk.Button(ventana2, text="Listar", command=mostrar_doctores)
btn_salir_doctores.place (x=285, y=580)

btn_salir_doctores = ttk.Button(ventana2, text="Salir", command=ventana.quit)
btn_salir_doctores.place (x=375, y=580)


#_________________________________PACIENTES BUSQUEDA__________________________________________#


def buscar_pacientes():
    conexion = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='sistemaclinicafinalparaprogramacion'
    )
    cursor = conexion.cursor()
    cuit = cuit_entry_pacientes.get()

    # Consulta SQL para buscar los registros con el CUIT especificado
    query = "SELECT * FROM pacientes WHERE cuit = %s"
    cursor.execute(query, (cuit,))
    resultados = cursor.fetchall()

    # Limpiar el Treeview antes de mostrar los nuevos resultados
    for i in tabla3.get_children():
        tabla3.delete(i)

    # Mostrar los resultados en el Treeview
    for resultado in resultados:
        tabla3.insert("", "end", values=resultado)
    cursor.close()

def actualizar_pacientes():
    # Limpiar el Treeview después de hacer clic en el botón "Actualizar"
    for i in tabla3.get_children():
        tabla3.delete(i)


# Crear la barra de búsqueda
cuit_label_pacientes = ttk.Label(ventana3, text="CUIT:")
cuit_label_pacientes.place(x=705,y=370)

cuit_entry_pacientes = ttk.Entry(ventana3)
cuit_entry_pacientes.place(x=662,y=395)
buscar_button_pacientes = ttk.Button(ventana3, text="Buscar", command=buscar_pacientes)
buscar_button_pacientes.place(x=685,y=425)

tabla3=ttk.Treeview(ventana3, height=15, columns=('#0','#1','#2','#3','#4','#5','#6','#7','#8','#9','#10','#11','#12'))

columnas = ['ID','Nombre', 'Apellido', 'Fecha Nacimiento', 'Género', 'CUIT', 'Celular', 'Correo Electrónico', 'Barrio', 'Calle', 'N° de Calle', 'País', 'Provincia']
tabla3["columns"] = columnas
tabla3["show"] = "headings"
for columna in columnas:
    tabla3.column(columna, width=100)
    tabla3.heading(columna, text=columna)
tabla3.pack()

# Crear el botón de actualización
actualizar_button = ttk.Button(ventana3, text="Actualizar", command=actualizar_pacientes)
actualizar_button.pack()


#_________________________________DOCTORES BUSQUEDA__________________________________________#


def buscar_medicos():
    conexion = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='sistemaclinicafinalparaprogramacion'
    )
    cursor = conexion.cursor()
    cuit = cuit_entry_medicos.get()

    # Consulta SQL para buscar los registros con el CUIT especificado
    query = "SELECT * FROM medicos WHERE cuit = %s"
    cursor.execute(query, (cuit,))
    resultados = cursor.fetchall()

    # Limpiar el Treeview antes de mostrar los nuevos resultados
    for i in tabla4.get_children():
        tabla4.delete(i)

    # Mostrar los resultados en el Treeview
    for resultado in resultados:
        tabla4.insert("", "end", values=resultado)
    cursor.close()

def actualizar_medicos():
    # Limpiar el Treeview después de hacer clic en el botón "Actualizar"
    for i in tabla4.get_children():
        tabla4.delete(i)


# Crear la barra de búsqueda
cuit_label_medicos = ttk.Label(ventana4, text="CUIT:")
cuit_label_medicos.place(x=705,y=370)

cuit_entry_medicos = ttk.Entry(ventana4)
cuit_entry_medicos.place(x=662,y=395)
buscar_button_medicos = ttk.Button(ventana4, text="Buscar", command=buscar_medicos)
buscar_button_medicos.place(x=685,y=425)

tabla4=ttk.Treeview(ventana4, height=15, columns=('#0','#1','#2','#3','#4','#5','#6','#7','#8','#9','#10','#11','#12','#13'))

columnas = ['ID','Nombre', 'Apellido', 'Fecha Nacimiento', 'Género', 'CUIT', 'Celular', 'Correo Electrónico', 'Barrio', 'Calle', 'N° de Calle', 'País', 'Provincia', "Especialidades"]
tabla4["columns"] = columnas
tabla4["show"] = "headings"
for columna in columnas:
    tabla4.column(columna, width=100)
    tabla4.heading(columna, text=columna)
tabla4.pack()

# Crear el botón de actualización
actualizar_button = ttk.Button(ventana4, text="Actualizar", command=actualizar_medicos)
actualizar_button.pack()



# Iniciar el bucle de la aplicación
ventana.mainloop()