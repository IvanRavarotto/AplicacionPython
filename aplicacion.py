#Se importan las librerias que seran utilizadas
from tkinter import *
from tkinter import messagebox
import sqlite3

'''--------------------------------------------------------------------- Funciones ---------------------------------------------------------------------'''

#Funcion para crear la base e informar si ya esta creada
def iniciarBase():
  #Se crea la base de datos
  #Se crea un trycatch por si ya existe y no rompa el programa
  try:
    baseDeDatos = sqlite3.connect("baseDeDatos")
    cursor = baseDeDatos.cursor()
    #Se crea la tabla
    cursor.execute("CREATE TABLE USUARIOS (ID INTEGER PRIMARY KEY AUTOINCREMENT, NOMBRE_USUARIO VARCHAR(50), PASSWORD VARCHAR(50), APELLIDO VARCHAR(20), DIRECCION VARCHAR(50), COMENTARIO VARCHAR(100))")
    baseDeDatos.commit()
    messagebox.showinfo("Base de datos", "La base de datos, fue creada con exito.")
  except:
    messagebox.showerror("Error", "La base de datos ya existe")

#Funcion para salir del programa
def salir():
  respuesta = messagebox.askyesno("question", "Esta por finalizar el programa ¿Estas seguro?")
  if respuesta == True:
    raiz.destroy()

#"Licencia" del programa
def licencia():
  messagebox.showinfo("Licencia", "Este programa es propiedad de: \n\n Iván Tomás Ravarotto \n\n Version: 0.1")

#Información adicional
def masInformacion():
  messagebox.showinfo("Información", "Este programa se creo como practica sobre python en tkinter y sqlite3. \n\n Espero que sea de su gusto.")

#Funcion para cargar/crear los datos en la base de datos
def crear():
  usuario = (espacioNombre.get(), espacioPassword.get(), espacioApellido.get(), espacioDireccion.get(), espacioComentario.get("1.0", END))
  baseDeDatos = sqlite3.connect("baseDeDatos")
  cursor = baseDeDatos.cursor()
  cursor.execute("INSERT INTO USUARIOS VALUES (NULL, ?, ?, ?, ?, ?)", usuario)
  baseDeDatos.commit()
  baseDeDatos.close()

def leer():
  baseDeDatos = sqlite3.connect("baseDeDatos")
  cursor = baseDeDatos.cursor()
  #se debe buscar por ID tambien
  entrada = espacioNombre.get()
  cursor.execute("SELECT * FROM USUARIOS WHERE NOMBRE_USUARIO = ?", (entrada, ))
  informacion = cursor.fetchall()
  #Se debe cargar los datos traidos en cada entrada}
  #Se crea un if por si encuentra información o no:
  if informacion:
      for i in informacion:
        espacioID.delete(0, END)
        espacioID.insert(0, i[0])
        espacioNombre.delete(0, END)
        espacioNombre.insert(0, i[1])
        espacioApellido.delete(0, END)
        espacioApellido.insert(0, i[3])
        espacioDireccion.delete(0, END)
        espacioDireccion.insert(0, i[4])
        espacioComentario.delete("1.0", END)
        espacioComentario.insert("1.0", i[5])
        baseDeDatos.close()
  else:
    entrada = espacioID.get()
    cursor.execute("SELECT * FROM USUARIOS WHERE ID = ?", (entrada, ))
    informacion = cursor.fetchall()
    baseDeDatos.close()
    if informacion:
      for i in informacion:
        espacioID.delete(0, END)
        espacioID.insert(0, i[0])
        espacioNombre.delete(0, END)
        espacioNombre.insert(0, i[1])
        espacioApellido.delete(0, END)
        espacioApellido.insert(0, i[3])
        espacioDireccion.delete(0, END)
        espacioDireccion.insert(0, i[4])
        espacioComentario.delete("1.0", END)
        espacioComentario.insert("1.0", i[5])
        baseDeDatos.close()
    else:
      messagebox.showerror("Error", "No se encontraron resultados por ID o Nombre. \n\nVerifique que la información cargada sea correcta")

def limpiar():
  espacioID.delete(0, END)
  espacioNombre.delete(0, END)
  espacioPassword.delete(0, END)
  espacioApellido.delete(0, END)
  espacioDireccion.delete(0, END)
  espacioComentario.delete("1.0", END)

'''--------------------------------------------------------------------- Apartado visual ---------------------------------------------------------------------'''
raiz = Tk(); #Se crea la raiz
menuBarra = Menu(raiz) #Creamos la barra donde estaran las opciones
raiz.config(menu=menuBarra, width=450, height=600) #damos un tamaño a la raiz y asignamos el menu
raiz.title("Aplicacion con base de datos")

'''--------------------------------------------------------------------- Menus ---------------------------------------------------------------------'''

#Creamos los correspondientes menus y sus opciones
#A su vez los comandos necesarios para cada uno
menuBase = Menu(menuBarra, tearoff=0) #Menu base de datos
menuBase.add_command(label="Conectar", command=iniciarBase)
menuBase.add_command(label="Salir", command=salir) 

menuBorrar = Menu(menuBarra, tearoff=0) #Menu limpiar formulario
menuBorrar.add_command(label="Limpiar formulario", command=limpiar)

menuAyuda = Menu(menuBarra, tearoff=0) #Menu de ayuda
menuAyuda.add_command(label="Licencia", command=licencia)
menuAyuda.add_command(label="Más información", command=masInformacion)

#Sumamos estos menus creados a la barra.

menuBarra.add_cascade(label="Base de datos", menu=menuBase)
menuBarra.add_cascade(label="Limpiar", menu=menuBorrar)
menuBarra.add_cascade(label="Ayuda", menu=menuAyuda)

#Se crean los campos para los datos

frame = Frame(raiz)
frame.pack()

'''--------------------------------------------------------------------- Apartado entradas ---------------------------------------------------------------------'''

#Se crean cada espacio de texto para recibir los datos.
espacioID = Entry(frame);
espacioID.grid(row=0, column=1, padx=15, pady=5)

espacioNombre = Entry(frame);
espacioNombre.grid(row=1, column=1, padx=15, pady=5)

espacioPassword = Entry(frame);
espacioPassword.grid(row=2, column=1, padx=15, pady=5)
espacioPassword.config(show="*")

espacioApellido = Entry(frame);
espacioApellido.grid(row=3, column=1, padx=15, pady=5)

espacioDireccion = Entry(frame);
espacioDireccion.grid(row=4, column=1, padx=15, pady=5)

#El espacio del comentario sera de tipo Text el cual poseera un stroll a la derecha
espacioComentario = Text(frame, width=30, height=10);
espacioComentario.grid(row=5, column=1, padx=15, pady=5)
scroll=Scrollbar(frame, command=espacioComentario.yview)
scroll.grid(row=5, column=2, sticky="nsew")
espacioComentario.config(yscrollcommand=scroll)

'''--------------------------------------------------------------------- Apartado labels ---------------------------------------------------------------------'''

#Se crean los labels con dada identificador para cada dato
labelID = Label(frame, text="ID: ")
labelID.grid(row=0, column=0, sticky="e", padx=15, pady=5)

labelNombre = Label(frame, text="Nombre: ")
labelNombre.grid(row=1, column=0, sticky="e", padx=15, pady=5)

labelPassword = Label(frame, text="Password: ")
labelPassword.grid(row=2, column=0, sticky="e", padx=15, pady=5)

labelApellido = Label(frame, text="Apellido: ")
labelApellido.grid(row=3, column=0, sticky="e", padx=15, pady=5)

labelDireccion = Label(frame, text="Dirección: ")
labelDireccion.grid(row=4, column=0, sticky="e", padx=15, pady=5)

labelComentario = Label(frame, text="Comentario: ")
labelComentario.grid(row=5, column=0, sticky="e", padx=5, pady=5)

#Se crean los botones
frame2 = Frame(raiz)
frame2.pack()

'''--------------------------------------------------------------------- Apartado botones ---------------------------------------------------------------------'''

#Boton crear/create
crearBoton = Button(frame2, text="Crear/Create", command=crear)
crearBoton.grid(row=0, column=0, sticky="e", padx=5, pady=5)

#Boton leer/read
leerBoton = Button(frame2, text="Leer/Read", command=leer)
leerBoton.grid(row=0, column=1, sticky="e", padx=5, pady=5)

#Boton actualizar/update
actualizarBoton = Button(frame2, text="Actualizar/Update")
actualizarBoton.grid(row=0, column=2, sticky="e", padx=5, pady=5)

#Boton borrar/delete
borrarBoton = Button(frame2, text="Borrar/Delete")
borrarBoton.grid(row=0, column=3, sticky="e", padx=5, pady=5)

raiz.mainloop();