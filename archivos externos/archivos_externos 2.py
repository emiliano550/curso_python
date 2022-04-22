#PUNTEROS -----> Es donde se posiciona el cursor

# MÉTODO seek() ----> NMos pedira un parametro que es numero de caracter o posición donde se colocara el puntero (CURSOR)

from io import open
archivo_texto = open('archivo.txt', 'r')

#archivo_texto.seek(11)   # seek ----> posiciona el puntero en el lugar donde le indicamos
#print(archivo_texto.read(11))  # read  ---> Realiza la lectura HASTA la posición que le indicamos y hasta ahi se detiene
#archivo_texto.seek(len(archivo_texto.read())/2)  # Para saber la longitd 
print(archivo_texto.read())

# Con el Método read(), EMPIEZA A LEER a partir del parametro introducido, tambien se puede colocar el puntero en una posición especifica, colocando dentro el parametro
#print(archivo_texto.read(11))


# MÉTODO READLINE -----> Lectura linea a linea
archivo_texto.seek(len(archivo_texto.readline()))   #Se coloca al final de la 1ra linea