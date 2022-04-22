#CONDICIONALES
#if :si
#else: y sino es verdad
#elif: 

#Para que haya un else, siempre tiene que haber un if, no puede haber 2 else dentro de un if
# El ultimo else, se va a acompañar o cumplir del if inmediato que se cumplio, por eso hay que revisar la logica

print('Verificación de acceso')

edad_usuario = int(input('Introduce tu edad: '))

if edad_usuario <=18:
    print('No puedes acceder, lo siento')
elif edad_usuario >100:
    print('Edad incorrecta')
else:
    print('Puedes pasar')

print('El programa ha finzalizado', '\n')


print('Calificación final: ')
calif = int(input('Introduce la nota obtenia en examen: '))

if calif <=5:
    print('Calificación no aprobatoria, no aprobaste la materia')

elif calif >10:
    print('Introduce calificación valida')

elif calif == 9:
    print('Excelente nota!')

elif calif == 10:
    print('Tuviste la mejor nota!')

else:
    print('Calificación aprobatoria, pasaste la materia')

print('Suerte!')

