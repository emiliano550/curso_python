#DICCIONARIOS

# Estructura de datos que nos permiten almacenar valores de diferentes tipo (enteros, cadenas de texto, decimales) e incluso listas y otros diccionarios.
# La principal caracteristica de los diccionarios es que los datos se almacenan asociados a una clave de tal forma que se crea una asociación de tipo CLAVE: VALOR, para cada elemento almacenado.
# Los elementos almacenados no estan ordenados. El orden es indiferente a la hora de almacenar información en un diccionario.
# Los diccionarios van entre llaves
#No puede haber dos claves iguales dentro de un Diccionario

midiccionario = {'Alemania':'Berlin', 'Francia':'Paris', 'Reino Unido':'Londres', 'Espana':'Madrid'}
print(midiccionario['Espana'])
print(midiccionario)


#AGREGAR ELEMENTOS A UN DICCIONARIO CONSTRUIDO:
midiccionario['Italia'] = 'Lisboa'
print(midiccionario)


#MODIFICAR O CAMBIAR VALORES EN UN DICCIONARIO:
midiccionario['Italia'] = 'Roma'
print(midiccionario)

#ELIMINAR ELEMENTOS: Metodo del
del midiccionario['Reino Unido']
print(midiccionario)

#COMBINANDO DIFERENTES TIPOS DE VALORES
calif = {'Universidad':'UNITEC','Facultad':'Ingeniería','Alumno':'Abraham','Matematicas':8, 'Historia':7.5, 'Fisica':9, 'Algebra':8.2, }
print(calif, '\n')


#USAR UNA TUPLA PARA ASIGNAR VALORES A UN DICCIONARIO
#Se accede a los valores de la tupla por sus indices
mitupla = ['Espana', 'Francia', 'Reino Unido', 'Alemania']
midiccionario= {mitupla[0]:'Madrid', mitupla[1]:'Paris', mitupla[2]:'Londres', mitupla[3]:'Berlin'}
print(midiccionario,'\n')

#ACCEDER A UN ELEMENTO:
print(midiccionario['Francia'], '\n')


#ACCEDER A UNA TUPLA ENTERA DE VALORES O ACCEDER A TODOS LOS VALORES DE UNA TUPLA
midiccionario = {23:'Jordan', 'Nombre':'Michael', 'Equipo':'Chicago', 'anillos':[1991, 1992, 1993, 1996, 1997, 1998]}
print(midiccionario, '\n')


#ACCEDER A UN VALOR
print(midiccionario['Equipo'])
print(midiccionario['anillos'],'\n')


#GUARDAR UN DICCIONARIO DENTRO DE OTRO DICCIONARIO
#Convertir el dato anillos en un diccionario de la siguiente forma:
# midiccionario = {23:'Jordan', 'Nombre':'Michael', 'Equipo':'Chicago', 'anillos':{'temporadas':[1991, 1992, 1993, 1996, 1997, 1998]}}
#Abriendo las llaves porque es un diccionario dentro de otro diccionario
#al imprimir anillos te arroja el diccionario completo de anillos : temporadas....


#CLAVE: VALOR

#METODO keys: NOS DEVUELVE LAS CLAVES DE UN DICCIONARIO
print(midiccionario.keys(), '\n')

#METODO value, NOS DEVUELVE LOS VALORES
print(midiccionario.values(), '\n')

#METODO len: NOS DEVUELVE LA LONGITUD
print(len(midiccionario))

print(midiccionario)











