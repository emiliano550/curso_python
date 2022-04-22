from io import open  # método open, apra abrir un archivo externo

# El método 'open' nos pide 2 agumentos: 1.nombre del archivo que queremos abrir & 2. el Modo(lectura, escritura, append) que lo queremos abrir
archivo_texto = open("archivo.txt", "r") # Modo lectura


#MÉTODO readlines()  -------> Nos permite leer la información que esta guardada en el archivo linea a linea y almacenar esa información en una lista
#Para realizar acciones de 'busqueda' y 'manipulación'
lineas_texto = archivo_texto.readlines()  #Esta variable se convierte en una 'lista manipulable'
archivo_texto.close()
print(lineas_texto)    #--------> Aqui podemos ver como nos imprime una lista ---->[]
print(lineas_texto[0])  # -------> Acceder a los elemenos de una lista con indices[0, 1, 2....] que en esta casi serian los renglones
print(lineas_texto[1])