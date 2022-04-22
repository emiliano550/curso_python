# CONDICIONALES
# Instrucción IF

#OPERADORES DE COMPARACIÓN:
# > mayor que
# < menor que
# == igual que
# >= mayor o igual que 
# <= menor o igual que 
# != diferente que

#def evaluacion(nota):
#    valoracion = 'aprobado'
#     if nota <5:
#        valoracion = 'reprobado'
#        return valoracion
#print(evaluacion(4))


#def apuesta(marcador):
#    resultado = 'ganador' or 'no ganadora'
#    if marcador > 2:
#        resultado = 'Ganador'
#        return resultado
#print(apuesta(3), '\n')


#print('Programa de evaluación de notas de alumnos')
import re


nota_alumno = input('Evaluación de notas de alumnos: ')

def evaluacion(nota):
    valoracion = 'aprobado'
    if nota <=5:
        valoracion = 'reprobado'
    return valoracion

print(evaluacion(int(nota_alumno)), '\n')

# Cualquier valor introducido en input() en python lo toma como texto(str)
# Funcion int(), transforma los valores en enteros, cuando usemos la función input()
# La función input(), puede aceptar parametros
# AMBITO de una Variable: Esto significa que las variables declaradas dentro de una función solo se pueden usar dentro de este bloque de codigo. Si se quiere usar o llamar esta variable fuera de este ambito, no funcionara

resultado = input('Resultado de apuesta mayor a 2 goles: ')

def apuesta(goles):
    marcador = 'ganador'
    if goles <=2: 
        marcador = 'no ganadora'
    return marcador
print(apuesta(int(resultado)), '\n')



resultado = input('Resultado apuesta menor a 3 goles: ')

def apuesta(goles):
    marcador = 'Apuesta No ganadora'
    if goles <= 3:
        marcador = 'Apuesta ganada'
    return marcador 
    
print(apuesta(int(resultado)), '\n')


print('Resultado de Calificaciones Finales: ')
calif = input('')

def historia(x):
    calificacion = 'Pasaste la materia'
    if x <= 8:
        calificacion = 'No aprobaste la materia'
    return calificacion
print(historia(int(calif)))

# x lo tomamos como calificacion




