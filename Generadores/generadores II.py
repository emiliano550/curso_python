# GENERADORES 
# Instrucción 'yield from'
# yield from: Utilidad para simplificar el código de los generadores en el caso de utilizar bucles anidados
#Tienes elementos dentro de un objeto
# Seria como un array de dos dimenciones



#En python cuando se coloca un '*' adelante del argumento de una función le estamos indicando que va a recibir un numero indeterminado de elementos Y DE FORMA DE 'tupla'
def devuelve_ciudades(*ciudades):
    for elemento in ciudades:
        for subelemento in elemento:
            yield subelemento 

ciudades_devueltas = devuelve_ciudades('Madrid', 'Barcelona', 'Bilbao', 'Valencia')
print(next(ciudades_devueltas))
print(next(ciudades_devueltas))
# Al primir, nos devuelve los 2 primeros sub elementos, del elemento: Ose la letra 'M' y 'a', del 1er elemento que es 'Madrid'
#La función 'Yield from' nos ayuda a simplificar el codigo de arriba. A continuación vemos como:

def devuelve_ciudades(*ciudades):
    for elemento in ciudades:
        yield from elemento # este yield from: Hazme un yield desde el 1er elemento

ciudades_devueltas = devuelve_ciudades('Madrid', 'Barcelona', 'Bilbao', 'Valencia')
print(next(ciudades_devueltas))
print(next(ciudades_devueltas))