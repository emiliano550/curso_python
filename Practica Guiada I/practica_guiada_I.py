from cgitb import text
from mimetypes import common_types
from struct import pack
from tkinter import*
from tkinter import messagebox
import sqlite3
from tokenize import String

root=Tk()

#-----------------------FRAME Superior---------------
miFrame=Frame(root)
miFrame.pack()

#-----------------------2DO FRAME Inferior-----------
misegundoFrame=Frame(root)
misegundoFrame.pack()

#-------------------------FUNCIONES DE VENTANAS EMERGENTES en MENUS y BOTONES----------
#Conexión a la BBDD
def conexionBBDD():
    miConexion=sqlite3.connect('Usuarios')
    miCursor=miConexion.cursor()

#Metemos la funcion en un try, y si es la 1ra vez que se ejeuta lo hara, y sino manara el otro mensaje
    try:
        miCursor.execute('''
            CREATE TABLE DATOSUSUARIOS (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            NOMBRE_USUARIO VARCHAR(30),
            PASSWORD VARCHAR(30),
            APELLIDO VARCHAR(30),
            DIRECCION VARCHAR(50),
            COMENTARIOS VARCHAR(100))
            ''')
        messagebox.showinfo('BBDD', 'BBDD creada con éxito')
    except:
        messagebox.showwarning('¡Atención!', 'La BBDD ya existe')

 #Función Salir-----------  
def salirApp():
    valor=messagebox.askquestion('Salir', '¿Desea Salir de la Aplicación?')
    if valor== 'yes':
        root.destroy()


#Esta función va a resetear los campos de los 'Entrys'
def limpiarCampos():
    miNombre.set('')   #Con esto establecemos el campo a una cadena vacia(osea se quita lo que este dentro)
    miId.set('')
    miApellido.set('')
    miDireccion.set('')
    miPass.set('')
    textoComentarios.delete(1.0, END)#Para borrar lo del cuadro de texto---->Método 'delete(1.0, END)'----->1.0=Punto de partido, osea borra desde el primer caracter hasta el Final(END)

#------------CREAR--------Informacion Introducida en los 'Entrys'---->SE INSERTE COMO UN NUEVO REGISTRO EN LA DB---->En el Ménu 'Crear' y con el boton 'Create'
def crear():
    miConexion=sqlite3.connect('Usuarios')   #debe conectar con la DB 'usuarios'
    miCursor=miConexion.cursor()

#Crearemos una CONSULTA PARAMETRIZADA
#Almacenamos en una variable la información de todos los campos--->miNombre.get,miPass....etc
    datos= miNombre.get(), miPass.get(), miApellido.get(), miDireccion.get(), textoComentarios.get("1.0", END)

    """miCursor.execute("INSERT INTO DATOSUSUARIOS VALUES(NULL, '" + miNombre.get() + 
        "','" + miPass.get() +
        "','" + miApellido.get() +
        "','" + miDireccion.get() +
        "','" + textoComentarios.get("1.0", END) +"')") """

    miCursor.execute("INSERT INTO DATOSUSUARIOS VALUES(NULL,?,?,?,?,?)",(datos))
    miConexion.commit()  # commit ------->Para que ejecute esta instrucción de tipo INSERT INTO
    messagebox.showinfo('BBDD', 'Registro insertado con éxito')



#Función Leer
#Sera una instruccion SELECT----> De esta forma la APP puede 'leer' la data
#Para que la data se pueda leer, lo haremos introduciendo el 'id' del usuario y nos debe aparecer la data del usuario
def leer():
    miConexion=sqlite3.connect('Usuarios')
    miCursor=miConexion.cursor()
    miCursor.execute("SELECT * FROM DATOSUSUARIOS WHERE ID=" + miId.get())

    elUsuario=miCursor.fetchall()     #Extraer la información de esta consulta
                                    #funcion 'fetchall'---> Nos devuelve un array con todos los rgistros que nos halla devuelto,  la consulta SQL 
    for usuario in elUsuario:
        miId.set(usuario[0])
        miNombre.set(usuario[1])
        miPass.set(usuario[2])
        miApellido.set(usuario[3])
        miDireccion.set(usuario[4])
        textoComentarios.insert(1.0, usuario[5]) #1.0---->Inserta la información desde el 1er caracter, hasta la posición 5
#[0], [1]---->Restaca la posicion que tenemos en el array(fetchall)
    miConexion.commit()  #Para que se ejecute


#Función UPDATE-------
def actualizar():
    miConexion=sqlite3.connect("Usuarios")
    miCursor=miConexion.cursor()
    datos= miNombre.get(), miPass.get(), miApellido.get(), miDireccion.get(), textoComentarios.get("1.0", END)

    """miCursor.execute("UPDATE DATOSUSUARIOS SET NOMBRE_USUARIO='" + miNombre.get() +
       "', PASSWORD='" + miPass.get() +
        "', APELLIDO='" + miApellido.get() +
        "', DIRECCION='" + miDireccion.get() +
        "', COMENTARIOS='" + textoComentarios.get("1.0", END) +
        "'WHERE ID=" + miId.get()) """

    miCursor.execute("UPDATE DATOSUSUARIOS SET NOMBRE_USUARIO= ?, PASSWORD=?,APELLIDO=?, DIRECCION=?, COMENTARIOS=? " +
        "WHERE ID=" + miId.get(), (datos))
    miConexion.commit()
    messagebox.showinfo('BBDD', 'Registro actualizado con éxito')

#Función ELIMINAR o DELETE
def eliminar():
    miConexion=sqlite3.connect('Usuarios')
    miCursor=miConexion.cursor()
    miCursor.execute("DELETE FROM DATOSUSUARIOS WHERE ID=" + miId.get())
    miConexion.commit()
    messagebox.showinfo('BBDD', 'Registro Borrado con éxito')



#-----------------------------MENUS----------------------------------
#Variable donde se va almacenar nuestro Menu y este se colocara en la parte superior de nuestra raiz (root)
barraMenu=Menu(root)
#Construimos el Menu
root.config(menu=barraMenu, width=300, height=300)

#Creamos las variables para definir cuantas opciones de Menu queremos y Agregamos opciones de SUBMENU
bbddMenu=Menu(barraMenu, tearoff=0)
bbddMenu.add_command(label='Conectar', command=conexionBBDD)
bbddMenu.add_command(label='Salir', command=salirApp)

borrarMenu=Menu(barraMenu, tearoff=0)
borrarMenu.add_command(label='Borrar Campos', command=limpiarCampos)


crudMenu=Menu(barraMenu, tearoff=0)
crudMenu.add_command(label='Crear', command=crear)
crudMenu.add_command(label='Leer', command=leer)
crudMenu.add_command(label='Actualizar', command=actualizar)
crudMenu.add_command(label='Borrar', command=eliminar)

ayudaMenu=Menu(barraMenu, tearoff=0)
ayudaMenu.add_command(label='Licencia')
ayudaMenu.add_command(label='Acerca de...')

#Especificamos los textos que van a llevar los MENUS
barraMenu.add_cascade(label='BBDD', menu=bbddMenu)
barraMenu.add_cascade(label='Borrar', menu=borrarMenu)
barraMenu.add_cascade(label='CRUD', menu=crudMenu)
barraMenu.add_cascade(label='Ayuda', menu=ayudaMenu)


#-----------------------------LABELS-------------------------
idLabel=Label(miFrame, text='Id:')
idLabel.grid(row=0, column=0, sticky='e', padx=10, pady=10)

nombreLabel=Label(miFrame, text='Nombre:')
nombreLabel.grid(row=1, column=0, sticky='e', padx=10, pady=10)

passwordLabel=Label(miFrame, text='Password:')
passwordLabel.grid(row=2, column=0, sticky='e', padx=10, pady=10)

apellidoLabel=Label(miFrame, text='Apellido:')
apellidoLabel.grid(row=3, column=0, sticky='e', padx=10, pady=10)

direccionLabel=Label(miFrame, text='Dirección:')
direccionLabel.grid(row=4, column=0, sticky='e', padx=10, pady=10)

comentariosLabel=Label(miFrame, text='Comentarios:')
comentariosLabel.grid(row=5, column=0, sticky='e', padx=10, pady=10)


#------------------------FUNCION 'StringVar'----> Para decirle a la APP que en cada 'Entry' se encontrara con una cadena de caracteres(StringVar)
#Para guardar los datos en la DB, resetear, que se Introducen en los 'Entry'----> cuadros de texto id, nombre..etc
miId=StringVar()
miNombre=StringVar()
miApellido=StringVar()
miPass=StringVar()
miDireccion=StringVar()
#Tenemos que asignar a cada 'Entry' la variable 'StrinVar' correspondiente----> como segundo parametro---->textvariable=miId

#------------------------------CUADROS DE ENTRADA--------------
cuadroId=Entry(miFrame, textvariable=miId)
cuadroId.grid(row=0, column=1, padx=10, pady=10)
cuadroId.config(fg='black', justify= 'left')

cuadroNombre=Entry(miFrame, textvariable=miNombre)
cuadroNombre.grid(row=1, column=1, padx=10, pady=10)
cuadroNombre.config(fg='blue', justify='right')
#fg=color frontal

cuadroPassword=Entry(miFrame, textvariable=miPass)
cuadroPassword.grid(row=2, column=1, padx=10, pady=10)
cuadroPassword.config(show='*',fg='black', justify='left')

cuadroApellido=Entry(miFrame, textvariable=miApellido)
cuadroApellido.grid(row=3, column=1, padx=10, pady=10)
cuadroApellido.config(fg='black', justify='left')

cuadroDireccion=Entry(miFrame, textvariable=miDireccion)
cuadroDireccion.grid(row=4, column=1, padx=10, pady=10)
cuadroDireccion.config(fg='black', justify='left')

#------------------------------CUADRO DE TEXTO--------------
textoComentarios=Text(miFrame, width=16, height=5)
textoComentarios.grid(row=5, column=1, padx=10, pady=10)

#----------------------------Barra de desplazamiento----
scrollVert=Scrollbar(miFrame, command=textoComentarios.yview)
scrollVert.grid(row=5, column=2, sticky='nsw')
textoComentarios.config(yscrollcommand=scrollVert.set) #Configuración del Scroll


#-----------------------------BOTONES--------------------------------
#Usando el FRAME 2
botonCreate=Button(misegundoFrame, text='Create', width=5, command=crear)
botonCreate.grid(row=0, column=0, sticky='e', padx=10, pady=10, columnspan=1)

botonRead=Button(misegundoFrame, text='Read', width=5, command=leer)
botonRead.grid(row=0, column=1, padx=10, pady=10, columnspan=1)

botonUpdate=Button(misegundoFrame, text='Update', width=5, command=actualizar)
botonUpdate.grid(row=0, column=2, padx=10, pady=10, columnspan=1)

botonDelete=Button(misegundoFrame, text='Delete', width=5, command=eliminar)
botonDelete.grid(row=0, column=3, padx=10, pady=10, columnspan=1)


root.mainloop()








#Aplicación gráfica CRUD

