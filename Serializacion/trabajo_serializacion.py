import pickle  
# importamos la biblioteca

lista_nombres=['Pedro', 'Ana', 'Maria', 'Isabel']


#Creación de un fichero externo, pero con escritura binaria
#Método open con su segundo argumento 'wb' write binary
fichero_binario=open('lista_nombres', 'wb')


#volcado de la lista a el fichero externo
# Usamos la biblioteca pickle y el método 'dump' y este método requiere dos argumentos
#1er argumento ----> fichero en memoria(lista_nombres) y 2do nombre del fichero al que lo queremos volcar
pickle.dump(lista_nombres, fichero_binario)
fichero_binario.close()

del(fichero_binario)