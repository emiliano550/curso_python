import sqlite3

miConexion=sqlite3.connect('GestionProductos_UNIQUE')
miCursor=miConexion.cursor()

#------------------------READ---------------------
#SELECCIONAMOS LOS CAMPOS CON querys SQL
#miCursor.execute("SELECT * FROM PRODUCTOS WHERE SECCION = 'confección'")

#productos=miCursor.fetchall()
#print(productos)    #Nos va a devolver la lista



#------------------------UPDDATE------------------
#miCursor.execute("UPDATE PRODUCTOS SET PRECIO=35 WHERE NOMBRE_ARTICULO ='pelota'")


#-------------------------DELETE--------------------------
miCursor.execute("DELETE FROM PRODUCTOS WHERE ID=5")




miConexion.commit()
miConexion.close()