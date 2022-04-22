# MÉTODOS DE CADENAS
# Como manipular cadenas(Strings) de caracteres

#STRING:
# upper(): Convierte en Mayusculas un string
# lower(): Convierte en minusculas un string
# capitalize(): Poner la 1ra letra en mayuscula
# count(): Cuenta, cuantas veces aparece una letra o una cadena de caracteres dentro de un texto/frase
# find(): Representa el indice(posición) en la cual aparece un caracter o un grupo de caracteres dentro de un texto
# isdigit(): Devuelve un valor booleano, si el valor introducido es un digito(valor númerico) o no lo es
# isalum(): Comprobar si son alfanumericos
# isalpha(): Comprobar si hay solo letras 
# split(): Separa por palabras utilizando espacios
# strip(): Borrar espacios sobrantes al principio y al final
# replace(): Cambia una palabra o letra por otra dentro de un string
# rfin(): Representa el indice(posición) de un caracter, empezando desde atras


nombreUsuario = input('Introduce tu nombre de Usuario: ')
print('El nombre es: ', nombreUsuario.upper())

primer_apellido = input('Introduce tu 1er apellido: ')
print('El apellido es: ', primer_apellido.lower())

segundo_apellido = input('Introduce tu 2do apellido: ')
print('El apellido es: ', segundo_apellido.capitalize())

edad = input('Introduce tu edad: ')
print(edad.isdigit())

#Hay que recordar que todo lo que introducimos con la fuinción input(), python lo toma como texto, por eso cuando querramos usar numeros, utilizamos int()

edad = input('Introduce la edad: ')

if int(edad) <18:
    print('No puede pasar')
else:
    print('Puedes pasar')











