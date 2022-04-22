edad = input('Introduce la edad: ')

while edad.isdigit() == False:
    print('Por favor Introduce un valor númerico')
    edad = input('Introduce la edad: ')


if int(edad) <18: 
    print('No puede pasar')
else:
    print('Puedes pasar')



calif = input('Introduce tu calificación: ')

while calif.isdigit() == False:
    print('Introduce tu calificación en valor numerico: ')
    calif = input('Introduce de nuevo tu calificación porque estas metiendo letras')

if int(calif) <6:
     print('Necesitas tener mas de 6 para pasar la materia')
     calif =input('Introduce de nuevo tu calificación: ')

if int(calif) >= 6:
    print('Muy bien has pasado la materia')

    