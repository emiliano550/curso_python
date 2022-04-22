from io import open

#VAMOS AGREGAR UNA 3RA LINEA DE TEXTO
archivo_texto = open('archivo.txt', 'a')# Pasamos 'a' de append para agregar, añadir información
archivo_texto.write('\n siempre es una buena ocasión para estudiar Python')
