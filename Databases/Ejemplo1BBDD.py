import sqlite3

#creamos la conexion utilizando la librearia sqlite3 y llamamos al método connect
miConexion=sqlite3.connect('PrimeraBase')

#Creamos el cursos para ------>Poder crear la 1ra Tabla
miCursor=miConexion.cursor()

#CREAMOS NUESTRA 1RA TABLA
#miCursor.execute('CREATE TABLE PRODUCTOS(NOMBRE_ARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20))')

#INSERTAMOS DATOS-----> DEBEMOS INVALIDAR LA TABLA sino generara un error y entonces la comentamos
miCursor.execute('INSERT INTO PRODUCTOS VALUES("BALON", 15, "DEPORTES")')
miConexion.commit()  #----> Método 'commit' para confirmar los cambios que se haran en la tabla, que en este caso es insertar registros 




#Cerramos la conexion de la DB con el método 'close'
miConexion.close()
