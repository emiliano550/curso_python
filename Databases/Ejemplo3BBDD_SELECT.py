import sqlite3

#creamos la conexion utilizando la librearia sqlite3 y llamamos al método connect
miConexion=sqlite3.connect('PrimeraBase')

#Creamos el cursos para ------>Poder crear la 1ra Tabla
miCursor=miConexion.cursor()

#SELECIONAR INFORMACIÓN ------> SELECT
miCursor.execute('SELECT*FROM PRODUCTOS')

#Creamos una variable donde se almacenara una lista para leerlo
variosProductos=miCursor.fetchall() #El método 'fetchall'----> nos devuelve una lista con todos los registros que nos devuelve la instrucción de SQL
#print(variosProductos)

#UTILIZAMOS 'for' PARA QUE RECORRA LA LISTA Y LO IMPRIMA PRODUCTO POR PRODUCTO
for producto in variosProductos:
#    print(producto)

#ACCEDER A CAMPOS ESPECIFICOS con los INDICES
    print('Nombre Articulo: ', producto[0], 'Sección: ', producto[2])  #----->Lo concatenamos
#En la tupla la posición 0 es---> NOMBRE ARTICULO y la posición 1 es ---> PRECIO y asi sucesivamente


miConexion.commit()  #----> Método 'commit' para confirmar los cambios que se haran en la tabla, que en este caso es insertar registros 

#video 57

691 + 1000
