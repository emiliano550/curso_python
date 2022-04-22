class Coche():                #clase  
  
    def __init__(self):      # Metodo constructor   

        self.__largoChasis = 250    # propiedades
        self.__anchoChasis=120
        self.__ruedas = 4          #ENCAPSULAMIENTO de la variable 'ruedas'     
        self.__enmarcha=False

    def arrancar(self, arrancamos):       
        self.enmarcha = arrancamos   

        if self.__enmarcha:
            return 'El coche esta en marcha'
        else:
            return 'El coche esta parado'

    def estado(self):
        print('El coche tiene ', self.__ruedas, 'ruedas. Un ancho de ', self.__anchoChasis, 'y un largo de ', self.__largoChasis)
       
miCoche=Coche()             
print(miCoche.arrancar(True)) 
miCoche.estado()

print('-------------A continuación creamos el segundo objeto-------------')

miCoche2 = Coche()
print(miCoche2.arrancar(False))  
miCoche2.__ruedas=2
miCoche2.estado()



# ENCAPSULAMIENTO: Es para proteger los valores de las propiedades de una clase, y que estas no se puedan modificar
# Para ENCAPSULAR una variable o propiedad, se tiene que colocar 2 guiones bajos(__), antes de la variable.
# Al encapsular la variable no es accesible desde el 'exterior de la clase', pero si es accesible desde el interior de la clase
# Para acceder a una variable ENCAPSULADA desde un 'Metodo' se tiene que escribir con los guines bajos(__)


# ESTADO INICIAL: Caracteristicas comunes de los objetos, forman parte de un estado inicial. Quiere decir que estas caracteristicas comunes sean como de fabrica, como 
# en el ejemplo del obejto 'carro' este por default, tiene un largo, ancho, estado parado y 4 ruedas.

# Para especificar el estado inicial de un obejto perteneciente a una clase lo hacemos con un "CONSTRUCTOR"
# CONSTRUCTOR: Es un metodo especial que le da un estado inicial a los objetos. Forma de especificar claramente cual va hacer el estado incial de los objetos que pertenecen a una clase.

# Para definir un metodo constructor:

# ------ def __init__(self):---   # Cuando escribes esto en python, estas definiendo que este va hacer tu constructor de tu clase. 

#Es el que le va a dar un estado iniciala los objetos que pertenecen a tu clase

