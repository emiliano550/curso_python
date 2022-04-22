import sqlite3

#creamos la conexion utilizando la librearia sqlite3 y llamamos al método connect
miConexion=sqlite3.connect('PrimeraBase')

#Creamos el cursos para ------>Poder crear la 1ra Tabla
miCursor=miConexion.cursor()


#INSERTAR UN LOTE DE REGISTROS-------->UTILIZANDO  ---->LISTAS Y TUPLAS
variosProductos=[
    ('Camiseta', 10, 'Deportes'),
    ('Jarron', 90, 'Ceramica'),
    ('Camion', 20, 'Jugueteria')
]

miCursor.executemany('INSERT INTO PRODUCTOS VALUES(?,?,?)',variosProductos)
#Tienes que colocar tantos signos de '?' de acuerdo al numero de registros que tienes, en este caso son 3


miConexion.commit()  #----> Método 'commit' para confirmar los cambios que se haran en la tabla, que en este caso es insertar registros 




#Cerramos la conexion de la DB con el método 'close'
miConexion.close()


# INSERCIÓN DE VARIOS REGISTROS
# RECUPERACIÓN DE VARIOS REGISTROS
