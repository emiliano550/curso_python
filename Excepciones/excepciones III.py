# EXCEPCIONES
# Lanzar excepciones 
# Instrucción 'raise'
# Creación de excepciones propias (más adelante en el curso cuando veamos la POO)

def evalua_edad(edad):
    if edad <0: 
        raise Mipropioerror('No se permiten edades negativas')  #Especificar el tipo de excepción que es....
    if edad <20:
        return 'Eres muy joven'
    elif edad <40:
        return 'Eres joven'
    elif edad <65:
        return 'Eres maduro'
    elif edad <100:
        return 'Cuidate...'
print(evalua_edad(-18))

#Hacer o crear una exepción cuando se cumpla una Condición





