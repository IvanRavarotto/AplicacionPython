''' -------------------------------------------------- Imports -------------------------------------------------- '''
#Se importan las librerias que seran utilizadas
from tkinter import *
from tkinter import messagebox
import sqlite3

''' -------------------------------------------------- Funciones -------------------------------------------------- '''
#Funcion crearBase()
#La misma se utilizara en el menu de "Base de datos", para crear la base de datos y/o notificar si la misma ya existe.
def crearBase():
  #Se genera un trycatch
  #Con el objetivo que primero se intente generar la base de datos y la misma ya cree la tabla con los valores que deben contener, por ejemplo: nombre del usuario.
  try:
    #Se crea la base de datos
    baseDeDatos = sqlite3.connect("baseDeDatos.db")
    #Se crea el cursor
    cursor = baseDeDatos.cursor()
    #Se crea la tabla con los valores de una ID autoincremental y que se asigna automaticamente, nombre del usuario, contraseña, apellido, direccion y un comentario sobre el mismo.
    cursor.execute("CREATE TABLE USUARIOS (ID INTEGER PRIMARY KEY AUTOINCREMENT, NOMBRE_USUARIO VARCHAR(50), PASSWORD VARCHAR(50), APELLIDO VARCHAR(20), DIRECCION VARCHAR(50), COMENTARIO VARCHAR(100))")
    #Se confirman la transacción
    baseDeDatos.commit()
    #Se imprime un mensaje de aviso que la base fue creada con exito.
    messagebox.showinfo("Base de datos", "La base de datos, fue creada con exito.")
  except:
    #En caso que la base ya exista, se informara con el siguiente mensaje
    messagebox.showerror("Error", "La base de datos ya existe")

#Funcion salir()
#La funcion salir permitira cerrar el programa en cuyo caso el usuario lo dese realizar asi.
def salir():
  #Se genera una pregunta junto a un mensaje para confirmar si realmente desea finalizar el programa
  respuesta = messagebox.askyesno("question", "Esta por finalizar el programa ¿Estas seguro?")
  #En caso que acepte, se cerrara el mismo, sino continuara ejecutandose
  if respuesta == True:
    raiz.destroy()

#Funcion licencia()
#Busca mostrar más que nada "información" basica sobre el programa en cuanto a quien lo creo.
def licencia():
  messagebox.showinfo("Licencia", "Este programa es propiedad de: \n\n Iván Tomás Ravarotto \n\n Version: 0.1")

#Funcion masInformacion()
#Brindara "información" adicional en cuanto al programa.
def masInformacion():
  messagebox.showinfo("Información", "Este programa se creo como practica sobre python en tkinter y sqlite3. \n\n Espero que sea de su gusto.")

#Funcion limpiar()
#solo funciona para limpiar el formulario.
def limpiar():
  espacioID.delete(0, END)
  espacioNombre.delete(0, END)
  espacioPassword.delete(0, END)
  espacioApellido.delete(0, END)
  espacioDireccion.delete(0, END)
  espacioComentario.delete("1.0", END)

#Funcion crear()
#Esta funcion se encargara de cargar los datos de un usuario con lo ingresado en el formulario
def crear():
  #Se genera una variable usuario que guarda lo ingresado en para entrada del formulario
  usuario = (espacioNombre.get(), espacioPassword.get(), espacioApellido.get(), espacioDireccion.get(), espacioComentario.get("1.0", END))
  #Se conecta con la base de dayos
  baseDeDatos = sqlite3.connect("baseDeDatos.db")
  #Se crea el cursor
  cursor = baseDeDatos.cursor()
  #Se cargan los datos en la tabla, con los valores ingresaros desde la variable usuario.
  cursor.execute("INSERT INTO USUARIOS VALUES (NULL, ?, ?, ?, ?, ?)", usuario)
  #Se confirma la transacción
  baseDeDatos.commit()
  #Se cierra la base de datos
  baseDeDatos.close()
  #Se imprime mensaje confirmando carga
  messagebox.showinfo("Carga", "Los datos fueron cargados con exito.")

#Funcion leer()
#Esta funcion busca permitir encontrar un usuario por nombre o ID y traer los datos del mismo.
def leer():
  #Se conecta con la base
  baseDeDatos = sqlite3.connect("baseDeDatos.db")
  #Se crea el cursor
  cursor = baseDeDatos.cursor()
  #Se obtiene primero el nombre del usuario.
  entrada = espacioNombre.get()
  #Se busca bajo el nombre
  cursor.execute("SELECT * FROM USUARIOS WHERE NOMBRE_USUARIO = ?", (entrada, ))
  #Se guarda la información sobre una variable.
  informacion = cursor.fetchall()
  #Se debe cargar los datos traidos en cada entrada
  #Se crea un if por si encuentra información o no:
  if informacion:
      for i in informacion:
        #Se limpia y se traen los datos guardados sobre la base.
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
  #En caso que no lo encuentre por usuario, se realizara la busqueda por ID
  else:
    #Se recupera la ID ingresada
    entrada = espacioID.get()
    #Se busca bajo ID
    cursor.execute("SELECT * FROM USUARIOS WHERE ID = ?", (entrada, ))
    #Se guardan los datos que se obtienen de la ID
    informacion = cursor.fetchall()
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
    #En cuyo caso no se encuentre por ID o usuario, se dara un mensaje de error informando que no hay resultados.
    else:
      messagebox.showerror("Error", "No se encontraron resultados por ID o Nombre. \n\nVerifique que la información cargada sea correcta")
  #Se cierra la base.
  baseDeDatos.close()

#Funcion actualizar()
#Es la que se utilizara para actualizar elementos
def actualizar():
  #Se conecta con la base de datos
  baseDeDatos = sqlite3.connect("baseDeDatos.db")
  #Se crea el cursor
  cursor = baseDeDatos.cursor()
  #Se guardan los valores ingresados "actualizados", en el formulario
  usuario = (espacioNombre.get(), espacioApellido.get(), espacioDireccion.get(), espacioComentario.get("1.0", END), espacioID.get());
  #Se actualiza la base de datos
  cursor.execute("UPDATE USUARIOS SET NOMBRE_USUARIO = ?, APELLIDO = ?, DIRECCION = ?, COMENTARIO = ? WHERE ID = ?", usuario)
  #Se confirma lso cambios
  baseDeDatos.commit()
  #Se gebera mensaje avisando que se actualizaron los datos con exito
  messagebox.showinfo("Actualizar", "Los datos fueron actualizados con exito.")
  #Se cierra la base de datos
  baseDeDatos.close()

  #Funcion eliminar()
  #Es la que se utilizara para eliminar elementos de la tabla.
def eliminar():
  #Se conecta con la base de datos
  baseDeDatos = sqlite3.connect("baseDeDatos.db")
  #Se crea el cursor
  cursor = baseDeDatos.cursor()
  #Se recupera la ID ingresada
  entrada = espacioID.get()
  #Se busca bajo ID y se elimina
  cursor.execute("DELETE FROM USUARIOS WHERE ID= ?", (entrada, ))
  #Se confirman los cambios
  baseDeDatos.commit()
  #Se genera mensaje dando aviso que se elimino el usuario con exito
  messagebox.showinfo("Eliminar", "Los datos fueron eliminados con exito.")
  #Se cierra la base.
  baseDeDatos.close()

''' -------------------------------------------------- Aplicación -------------------------------------------------- '''

raiz = Tk(); #Se crea la raiz
menuBarra = Menu(raiz) #Creamos la barra donde estaran las opciones
raiz.config(menu=menuBarra, width=450, height=600) #damos un tamaño a la raiz y asignamos el menu
raiz.title("Aplicacion con base de datos")

''' -------------------------------------------------- Menus -------------------------------------------------- '''

#Creamos los correspondientes menus y sus opciones
#A su vez los comandos necesarios para cada uno
menuBase = Menu(menuBarra, tearoff=0) #Menu base de datos
menuBase.add_command(label="Crear base", command=crearBase)
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

''' -------------------------------------------------- Campos de datos -------------------------------------------------- '''

#Se crean los campos para los datos
frame = Frame(raiz)
frame.pack()

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

''' -------------------------------------------------- Labels -------------------------------------------------- '''

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

''' -------------------------------------------------- Botones -------------------------------------------------- '''

#Se crean los botones
frame2 = Frame(raiz)
frame2.pack()

#Boton crear/create
crearBoton = Button(frame2, text="Crear/Create", command=crear)
crearBoton.grid(row=0, column=0, sticky="e", padx=5, pady=5)

#Boton leer/read
leerBoton = Button(frame2, text="Leer/Read", command=leer)
leerBoton.grid(row=0, column=1, sticky="e", padx=5, pady=5)

#Boton actualizar/update
actualizarBoton = Button(frame2, text="Actualizar/Update", command=actualizar)
actualizarBoton.grid(row=0, column=2, sticky="e", padx=5, pady=5)

#Boton borrar/delete
borrarBoton = Button(frame2, text="Borrar/Delete", command=eliminar)
borrarBoton.grid(row=0, column=3, sticky="e", padx=5, pady=5)

raiz.mainloop();