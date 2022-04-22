import sqlite3

miConexion=sqlite3.connect('GestionProductos')
miCursor=miConexion.cursor()

#Creamos Yabla con 4 Campos----> Con PRIMARY KEY
miCursor.execute('''
    CREATE TABLE PRODUCTOS (
        CODIGO_ARTICULO VARCHAR(4) PRIMARY KEY,
        NOMBRE_ARTICULO VARCHAR(50),
        PRECIO INTEGER,
        SECCION VARCHAR(20))
''')

#Creamos una Lista con Tuplas en su interior
productos= [
    ('AR01', 'pelota', 20, 'Juguteria'),
    ('AR02', 'pantalon', 15, 'confección'),
    ('AR03', 'destornillador', 25, 'ferreteria'),
    ('AR04', 'jarrón', 45, 'ceramica')
]

#Para ejecutar el script y nos cree la DB con la tabla, utilizamos ----> 'executemany'
#El 1er Parametro utilizamos signos de ? ----> que son los campos que vamos insertar---> ('AR01', 'pelota', 20, 'Juguteria')
#El 2do Parametro es el nombre de la lista ----> 'productos'
miCursor.executemany('INSERT INTO PRODUCTOS VALUES (?,?,?,?)', productos)



miConexion.commit()
miConexion.close()