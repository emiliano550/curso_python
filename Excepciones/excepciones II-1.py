
def divide():
    try:
        op1 = (float(input('Introduce el primer número: ')))
        op2 = (float(input('Introduce el segundo número: ')))

        print('La división es: ' + str(op1/op2))

    except ValueError:
        print('El valor introducido es erróneo')
    
    except ZeroDivisionError:
        print('No se puede dividir entre 0')

    finally:
        print('Calculo finalizado') # Lo que se introduzca adentro del 'finally' se va a ejecutar siempre, tanto si ocurre o no la excepción

divide()
# En python podemos utilizar varias clausulas except, de forma consecutivas para capturar las excepciones


# TAMBIEN PODEMOS COLOCAR LOS 'except' DE LA SIGUIENTE FORMA:


def divide():
    try:
        op1 = (float(input('Introduce el primer número: ')))
        op2 = (float(input('Introduce el segundo número: ')))

        print('La división es: ' + str(op1/op2))

    except:
        print('Ha ocurrido un error') # Se puede colocar un 'except' de forma generica, pero no es recomendable porque no se especifica cual fue la excepción
    

    print('Calculo finalizado \n')