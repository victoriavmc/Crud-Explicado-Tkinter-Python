######### IMPORTAR TODOS LOS MODULOS#################
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
##############################################
import os
##############################################
# Base de datos
import mysql.connector
################################################
# Conectar con la base de datos
################################################
# Creamos la conexion
cnx = mysql.connector.connect(
    user='root', password='', database='sistemaclinicaFinal')
# Creamos la consulta
cursor = cnx.cursor()


def soloVerTablas():
    # Mostrar tablas
    cursor.execute("show tables")
    # Mostrar tablas
    for x in cursor:
        print(x)
#################################################
# Creacion de la ventana *Titulo, Tamaño, Fondo


def crearVentana():
    global ventana
    ventana = Tk()
    ventana.title('Clinica')
    ventana.geometry('900x800')
    # Ico
    # Obtén la ruta absoluta del directorio actual  
    carpetaDeTodosLosArchivos = os.path.dirname(__file__)
    # Navega hacia la carpeta anterior
    carpetaLogo = os.path.join(carpetaDeTodosLosArchivos, "..","Iconos")
    # Construye la ruta completa de la imagen
    image_path = os.path.join(carpetaLogo, 'perropepsi.ico')
    # Establece el ícono de la ventana
    ventana.iconbitmap(image_path)
    barraDeMenu()

###############################################
# Cerrar la ventana actual y Mostrar la primera selección en la nueva ventana

def reiniciarApp():
    ventana.destroy()
    menuINICIO()
    messagebox.showinfo("Volver a empezar",
                        "La aplicación ha sido reiniciada.")

# Creación de la barra de menú y Menú de inicio


def barraDeMenu():
    menubar = Menu(ventana)
    ventana.config(menu=menubar)
    #
    menubasedat = Menu(menubar, tearoff=0)
    menubasedat.add_command(label="Reiniciar", command=reiniciarApp)
    menubar.add_cascade(label='Inicio', menu=menubasedat)

##############################################
# Para sobre poner cada seleccion debo tapar el texto anterior


def tapaFrame(frame, ptexto):
    Label(frame, bg="white", width=68, height=24).place(x=3, y=0)
    frame.configure(text=f"Bienvenido al sistema de {ptexto}")
    Label(frame, text="Seleccionar:").place(x=190, y=20)

# ACA HAY VARIOS IF ANIDADOS, GUIA DE RADIOBUTTON


def menuINICIO():
    crearVentana()
    # Creacion de Frame (Es el cuadro al rededor, queda estetico.)
    frame = LabelFrame(
        ventana, text="Bienvenido al sistema de Clínica", width=700, height=700)
    frame.pack()
    # Crea la seleccion de rol para especificar que menu usar.
    Label(frame, text="Seleccione su rol:").place(x=190, y=20)
    # Variable que tomara un valor segun lo que seleccione
    defineRol = IntVar()
    # Funcion cuando seleccione una de las opciones

    def obtenerRol():
        if defineRol.get() == 1:
            tapaFrame(frame, "Administradores")

            defineAccion = IntVar()

            def obtenerActividades():
                if defineAccion.get() == 1:
                    tapaFrame(frame, "Pacientes")

                    pacienteAccion = IntVar()

                    def pacientesAcciones():
                        tapaFrame(frame, "CRUD")
                        if pacienteAccion.get() == 1:
                            # ACA ARMAR ALGO CON Mysql (Tengo la tabla entidad y luego se especifica la tabla paciente):
                            print("Ingreso al CRUD de pacientes")

                            # Claves/Variables que ingresara, voy a definirlas.
                            nombre = StringVar()
                            apellido = StringVar()
                            fechaNacimiento = StringVar()
                            genero = StringVar()
                            cuit = StringVar()
                            telefonoCelular = StringVar()
                            correoElectronico = StringVar()
                            barrio = StringVar()
                            calle = StringVar()
                            numero = StringVar()
                            pais = StringVar()
                            provincia = StringVar()
                            ###

                            def cargarDatos():
                                nombre_val = nombre.get()
                                apellido_val = apellido.get()
                                fecha_nacimiento_val = fechaNacimiento.get()
                                genero_val = genero.get()
                                cuit_val = cuit.get()
                                telefono_celular_val = telefonoCelular.get()
                                correo_electronico_val = correoElectronico.get()
                                barrio_val = barrio.get()
                                calle_val = calle.get()
                                numero_val = numero.get()
                                pais_val = pais.get()
                                provincia_val = provincia.get()
                                # Ingresa los datos obtenidos a la tabla entidad
                                query = "INSERT INTO entidades (nombre, apellido, fecha_nacimiento, genero, cuit, telefono_celular, correo_electronico, barrio, calle, numero, pais, provincia) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                                valores = (nombre_val, apellido_val, fecha_nacimiento_val, genero_val, cuit_val, telefono_celular_val,
                                           correo_electronico_val, barrio_val, calle_val, numero_val, pais_val, provincia_val)

                                try:
                                    cursor.execute(query, valores)
                                    cnx.commit()
                                    messagebox.showinfo(
                                        "Éxito", "Los datos se han guardado correctamente en la base de datos.")
                                except mysql.connector.Error as error:
                                    messagebox.showerror(
                                        "Error", f"No se pudo guardar los datos en la base de datos: {error}")

                            # # Labels y Entrys
                            Label(frame, text="Ingrese los datos").place(
                                x=190, y=20)
                            Label(frame, text="Nombre").place(x=50, y=50)
                            Label(frame, text="Apellido").place(x=50, y=100)
                            Label(frame, text="Fecha de Nacimiento").place(
                                x=250, y=50)
                            Label(frame, text="Genero").place(x=250, y=100)
                            Label(frame, text="Cuit").place(x=50, y=150)
                            Label(frame, text="Telefono/Celular").place(x=50, y=200)
                            Label(frame, text="Correo Electronico").place(
                                x=250, y=150)
                            Label(frame, text="Barrio").place(x=250, y=200)
                            Label(frame, text="Calle").place(x=50, y=250)
                            Label(frame, text="Numero").place(x=50, y=300)
                            Label(frame, text="Pais").place(x=250, y=300)
                            Label(frame, text="Provincia").place(x=250, y=300)

                            # Nombre
                            entrada1 = Entry(frame, textvariable=nombre)
                            entrada1.place(x=90, y=80)
                            # Apellido
                            entrada2 = Entry(frame, textvariable=apellido)
                            entrada2.place(x=90, y=120)
                            # Fecha de nacimiendo
                            entrada3 = Entry(
                                frame, textvariable=fechaNacimiento)
                            entrada3.place(x=300, y=80)
                            # Genero
                            entrada4 = Entry(frame, textvariable=genero)
                            entrada4.place(x=300, y=120)
                            # Cuit
                            entrada5 = Entry(frame, textvariable=cuit)
                            entrada5.place(x=90, y=150)
                            # Telefono&Celular
                            entrada6 = Entry(
                                frame, textvariable=telefonoCelular)
                            entrada6.place(x=90, y=205)
                            # Correo electronico
                            entrada7 = Entry(
                                frame, textvariable=correoElectronico)
                            entrada7.place(x=300, y=155)
                            # Barrio
                            entrada8 = Entry(frame, textvariable=barrio)
                            entrada8.place(x=300, y=205)
                            # calle
                            entrada9 = Entry(frame, textvariable=calle)
                            entrada9.place(x=90, y=255)
                            # Numero
                            entrada10 = Entry(frame, textvariable=numero)
                            entrada10.place(x=90, y=305)
                            # Pais
                            entrada11 = Entry(frame, textvariable=pais)
                            entrada11.place(x=300, y=305)
                            # Provincia
                            entrada12 = Entry(frame, textvariable=provincia)
                            entrada12.place(x=300, y=305)

                            tkinter.Button(frame, text='Cargar datos', command=cargarDatos).place(
                                x=100, y=400)

                        elif pacienteAccion.get() == 2:
                            print("Baja")
                        elif pacienteAccion.get() == 3:
                            print("Modificación")
                        elif pacienteAccion.get() == 4:
                            print("Eliminar")
                        else:
                            print("Listar")

                    Radiobutton(frame, text="Alta", variable=pacienteAccion,
                                value=1, command=pacientesAcciones).place(x=50, y=50)
                    Radiobutton(frame, text="Baja", variable=pacienteAccion,
                                value=2, command=pacientesAcciones).place(x=50, y=100)
                    Radiobutton(frame, text="Modicacion", variable=pacienteAccion,
                                value=3, command=pacientesAcciones).place(x=50, y=150)
                    Radiobutton(frame, text="Eliminar", variable=pacienteAccion,
                                value=4, command=pacientesAcciones).place(x=50, y=200)
                    Radiobutton(frame, text="Listar", variable=pacienteAccion,
                                value=5, command=pacientesAcciones).place(x=50, y=250)
                else:
                    tapaFrame(frame, "Médicos")

                    medicosAccion = IntVar()

                    def medicosAcciones():
                        tapaFrame(frame, "CRUD")
                        if medicosAccion.get() == 1:
                            # ACA ARMAR ALGO CON Mysql (Tengo la tabla entidad y luego se especifica la tabla medicos, se agrega tres tablas más):
                            print("Alta")
                        elif medicosAccion.get() == 2:
                            print("Baja")
                        elif medicosAccion.get() == 3:
                            print("Modificación")
                        elif medicosAccion.get() == 4:
                            print("Eliminar")
                        else:
                            print("Listar")

                    Radiobutton(frame, text="Alta", variable=medicosAccion,
                                value=1, command=medicosAcciones).place(x=50, y=50)
                    Radiobutton(frame, text="Baja", variable=medicosAccion,
                                value=2, command=medicosAcciones).place(x=50, y=100)
                    Radiobutton(frame, text="Modicacion", variable=medicosAccion,
                                value=3, command=medicosAcciones).place(x=50, y=150)
                    Radiobutton(frame, text="Eliminar", variable=medicosAccion,
                                value=4, command=medicosAcciones).place(x=50, y=200)
                    Radiobutton(frame, text="Listar", variable=medicosAccion,
                                value=5, command=medicosAcciones).place(x=50, y=250)

            Radiobutton(frame, text="Pacientes", variable=defineAccion,
                        value=1, command=obtenerActividades).place(x=50, y=50)
            Radiobutton(frame, text="Médicos", variable=defineAccion,
                        value=2, command=obtenerActividades).place(x=50, y=100)
        else:
            tapaFrame(frame, "Médicos")
            selecciono = IntVar()
            # CONSULTAR CON LOS PROFESORES

            def menuMedico():
                if 1 == selecciono.get():
                    mensaje = "Ver Lista de Turnos por Médico."
                Message(frame, justify=CENTER, text=f"Haz seleccionado:\n{mensaje}",
                        bg="rosybrown").place(x=60, y=250)

            Radiobutton(frame, text="⫸ Ver Lista de Turnos por Médico.",
                        variable=selecciono, value=1, command=menuMedico).place(x="50", y="100")

    Radiobutton(frame, text="⫸ Administrador", variable=defineRol,
                value=1, command=obtenerRol).place(x=50, y=50)
    Radiobutton(frame, text="⫸ Médico", variable=defineRol,
                value=2, command=obtenerRol).place(x=50, y=100)


#####################################################
# Crea la ventana principal y Mostrar la primera selección
menuINICIO()
# Ejecuta
ventana.mainloop()
