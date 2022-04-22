import sqlite3

miConexion=sqlite3.connect('GestionProductos_UNIQUE')
miCursor=miConexion.cursor()

#Creamos Tabla con 4 Campos----> Con PRIMARY KEY y AUTOINCREMENT y UNIQUE
#Cláusulas UNIQUE-----> Para que los Campos NO REPITAN INFORMACION
miCursor.execute('''
    CREATE TABLE PRODUCTOS (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        NOMBRE_ARTICULO VARCHAR(50) UNIQUE,
        PRECIO INTEGER,
        SECCION VARCHAR(20))
''')

#Creamos una Lista con Tuplas en su interior
productos= [
    ('pelota', 20, 'Juguteria'),
    ('pantalon', 15, 'confección'),
    ('destornillador', 25, 'ferreteria'),
    ('jarrón', 45, 'ceramica'),
    ('pantalones', 35, 'confección')
]

#Para ejecutar el script y nos cree la DB con la tabla, utilizamos ----> 'executemany'
#El 1er Parametro utilizamos signos de ? ----> que son los campos que vamos insertar---> (NULL, 'pelota', 20, 'Juguteria')--> 
#Colocamos 'NULL' porque asi le indicamos que el 1er campo ID---> Es una 'PRIMARY KEY AUTOINCREMENT'
#El 2do Parametro es el nombre de la lista ----> 'productos'
miCursor.executemany('INSERT INTO PRODUCTOS VALUES (NULL,?,?,?)', productos)



miConexion.commit()
miConexion.close()







#Cláusulas UNIQUE-----> Para que los Campos NO REPITAN INFORMACION
#Operaciones CRUD(Cread, Read, Update, Delete)

