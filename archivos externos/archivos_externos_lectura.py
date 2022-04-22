from io import open  # método open, apra abrir un archivo externo

# El método 'open' nos pide 2 agumentos: 1.nombre del archivo que queremos abrir & 2. el Modo(lectura, escritura, append) que lo queremos abrir
archivo_texto = open("archivo.txt", "r") # Modo lectura

texto = archivo_texto.read() #Almacenamos lo que se lee, del archivo texto

archivo_texto.close() #cerramos el archivo
print(texto)



#MÉTODO readlines()  -------> Nos permite leer la información que esta guardada en el archivo linea a linea y almacenar esa información en una lista
#Para realizar acciones de 'busqueda' y 'manipulación'
