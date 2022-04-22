# CONDICIONALES
#AND: y si ademas
#OR: o si no....

# PROGRAMA PARA OTORGAR BECAS
# usando los siguientes requisitos
# distancia > 40 km
# numero de hermanos > 2
# salario familiar <= 20000
# Cumpliendo las condiciones de arriba

print('Programa de becas 2022')

distancia_escuela = int(input('Introduce la distancia a la escuela en km: '))
print(distancia_escuela)

numero_hermanos = int(input('Introduce el numero de hermanos en el centro: '))
print(numero_hermanos)

salario_familia = int(input('Introduce Salario anual bruto: '))
print(salario_familia)

if distancia_escuela  > 40 and numero_hermanos > 2 or salario_familia <= 20000:
    print('Tienes derecho a Beca, Felicidades!', '\n')
else:
    print('No tienes derecho a Beca', '\n')


# OPERADOR IN
# CASE SENSITIVE: Hay que tener cuidado porque Python identifica mayusculas de minusculas y acentos(de preferencia no colocar)
# FUNCIÓN lower():Transforma un valor a minusculas
# FUNCIÓN upper(): Transforma un valor a mayusculas
# Para usar la funcion lower() o upper(), solo tenemos que conbinar con una variable con un punto(.)......
# Ejemplo: asignatura = opcion.lower()

print('Asignaturas optativas 2022')

print('Asignaturas optativas: Informatica grafica - Pruebas de Software - Usabilidad y Accesibilidad')


opcion = input('Escribe la asignatura escogida: ')
asignatura = opcion.lower()

if asignatura in ('informatica grafica', 'pruebas de software', 'usabilidad y accesibilidad'):
    print('Asignatura elegida: ' + asignatura)
else:
    print('La asignatura escogida no esta contemplada', '\n')


print('Selecciona el sabor de tu Helado')
print('Helados de: Chocolate - Vainilla, Fresa, Limon, Cafe')
helado = input('Escribe el sabor del Helado que quieres: ')
sabor = helado.lower()

if sabor in('chocolate', 'vainilla', 'Fresa', 'limon', 'cafe'):
    print('Helado sabor: ' + sabor)
else:
    print('Selecciona un sabor de la lista, por favor')







