import sqlite3

miConexion=sqlite3.connect('GestionProductos')
miCursor=miConexion.cursor()

#Insertamos un nuevo valor en la tabla
miCursor.execute("INSERT INTO PRODUCTOS VALUES ('AR03', 'tren', 15, 'jugueteria')")


miConexion.commit()
miConexion.close()