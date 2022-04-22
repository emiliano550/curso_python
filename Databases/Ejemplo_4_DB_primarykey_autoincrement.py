import sqlite3

miConexion=sqlite3.connect('GestionProductos_PK_A')
miCursor=miConexion.cursor()

#Creamos Tabla con 4 Campos----> Con PRIMARY KEY y AUTOINCREMENT
miCursor.execute('''
    CREATE TABLE PRODUCTOS (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        NOMBRE_ARTICULO VARCHAR(50),
        PRECIO INTEGER,
        SECCION VARCHAR(20))
''')

#Creamos una Lista con Tuplas en su interior
productos= [
    ('pelota', 20, 'Juguteria'),
    ('pantalon', 15, 'confección'),
    ('destornillador', 25, 'ferreteria'),
    ('jarrón', 45, 'ceramica')
]

#Para ejecutar el script y nos cree la DB con la tabla, utilizamos ----> 'executemany'
#El 1er Parametro utilizamos signos de ? ----> que son los campos que vamos insertar---> (NULL, 'pelota', 20, 'Juguteria')--> 
#Colocamos 'NULL' porque asi le indicamos que el 1er campo ID---> Es una 'PRIMARY KEY AUTOINCREMENT'
#El 2do Parametro es el nombre de la lista ----> 'productos'
miCursor.executemany('INSERT INTO PRODUCTOS VALUES (NULL,?,?,?)', productos)



miConexion.commit()
miConexion.close()