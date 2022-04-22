# CONDICIONALES
# xxxSwitchxxx... No existe en python
#Concatenación de operadores de comparación
# Oeradores logicos "and" y "or"
# Operador "in"


#edad = 125

#if 0< edad <100:
#    print('Edad es correcta')
#else:
#    print('Edad incorrecta')

#CONTATENANDO OPERADORES DE COMPARACIÓN
salario_presidente = int(input('Introduce Salario presidente: '))
print('Salario Presidente: ' + str(salario_presidente), '\n')

salario_director = int(input('Introduce salario director: '))
print('Salario Director: ' + str(salario_director), '\n')

salario_jefe_area = int(input('Introduce Salario Jefe de Área: '))
print('Salario Jefe de Área: ' + str(salario_jefe_area), '\n')

salario_administrativo = int(input('Introduce salario Administrativo: '))
print('Salario administrativo: ' + str(salario_administrativo), '\n')

if salario_administrativo < salario_jefe_area < salario_director < salario_presidente:
    print('Todo funciona correctamente')
else:
    print('Algo falla en esta empresa')
