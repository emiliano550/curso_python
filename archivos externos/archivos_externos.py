from io import open  # método open, apra abrir un archivo externo

# El método 'open' nos pide 2 agumentos: 1.nombre del archivo que queremos abrir & 2. el Modo(lectura, escritura, append) que lo queremos abrir
archivo_texto = open("archivo.txt", "w") # w -----> write(escritura)

frase = 'Estupendo dia para estudiar Python \nel martes'
archivo_texto.write(frase)
archivo_texto.close()


# ARCHIVOS EXTERNOS

#Como trabajar con ficheros externos de texto con el módulo standar de python 'io'

#OBJETIVO: Persistencia de datos

#DOS ALTERNATIVAS:
# ------> Manejo de archivos externos(BINARIOS, TEXTO PLANO )
# ------> Trabajo con BBDD 


# MANEJO DE ARCHIVOS EXTERNOS
# FASES NECESARIAS PARA GUARDAR INFORMACIÓN EN ARCHIVOS EXTERNOS

#CREACION  ---> APERTURA ---> MANIPULACION ---> CIERRE

#Descarga del modulo 'io