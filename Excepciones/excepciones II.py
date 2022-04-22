# EXCEPCIONES

# Capturas de varias exepciones
# Cláusula finally

def multiplica(num1, num2):
    return num1*num2

def divide(num1, num2):
    try:
        return num1/num2
    except ZeroDivisionError: #Si dividemos /0 nos dara el siguiente error, por eso hay que poner la exepción
        print('No se puede dividir entre 0')
        return 'Operación errónea'

def suma(num1, num2):
    return num1 + num2

def resta(num1, num2):
    return num1 - num2

while True:
    try:
        op1 = int(input('Introduce el primer número: '))
        op2 = int(input('Introduce el segundo número: '))
        break # Si se introducen los numeros no pasa por except(se lo brinca) y pasa a operación
    except ValueError:
        print('Los valores introducidos no son correctos')

operacion = input('Introduce la operación a realizar (suma, resta, multiplica, divide):  ')

if operacion == 'suma':
    print(suma(op1, op2))

elif operacion == 'resta':
    print(resta(op1, op2))

elif operacion == 'multiplica':
    print(multiplica(op1, op2))

elif operacion == 'divide':
    print(divide(op1, op2))

else: 
    print('Operación no contemplada')

print('Operación ejecutada. Continuación de ejecución del programa ')
# Si el programa se ejecuta pero hay un error, no podra seguir el programa, pero si queremos que siga aplicamos una 'exepcion':

# captura o control de excepcion

#min 5