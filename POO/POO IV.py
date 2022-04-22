# CONSTRUCTORES 
#CREAREMOS UN 2DO OBJETO QUE PERTENECE A LA MISMA CLASE

class Coche():           #clase  
    largoChasis = 250    # propiedades
    anchoChasis=120
    ruedas = 4
    enmarcha=False

                               #Caracteristicas de un metodo(comportamiento): def, nombre de la función, parametro por defecto llamado 'self(objeto perteneciente a la clase o instancia perteneciente a la clase)',pass 
    def arrancar(self, arrancamos):        #Los metodos se definen de esta forma, porque son una función que pertenecen a una clase. Y las funciones normales no pertenecen a una clase.
        self.enmarcha = arrancamos   #self es = a el objeto que en este caso es 'miCoche'

        if self.enmarcha:
            return 'El coche esta en marcha'
        else:
            return 'El coche esta parado'

    def estado(self):
        print('El coche tiene ', self.ruedas, 'ruedas. Un ancho de ', self.anchoChasis, 'y un largo de ', self.largoChasis)
       

miCoche=Coche()              #Definimos nuestro objeto y el nombre de la clase a la que pertenece el objeto/instancia. INSTANCIAR UNA CLASE 
#print('El largo de mi coche es: ',miCoche.largoChasis)
#print('El coche tiene', miCoche.ruedas, 'ruedas')
print(miCoche.arrancar(True)) #aqui colocamos True el parametro de la función arrancar

miCoche.estado()


print('-------------A continuación creamos el segundo objeto-------------')
#Crearemos nuestra segunda instancia/ Objeto

miCoche2 = Coche()
#print('El largo de mi coche es: ', miCoche2.largoChasis)
#print('El coche tiene ',miCoche2.ruedas, ' ruedas')
print(miCoche2.arrancar(False))  #aqui colocamos False el parametro de la función arrancar
miCoche2.estado()



# ESTADO INICIAL: Caracteristicas comunes de los objetos, forman parte de un estado inicial. Quiere decir que estas caracteristicas comunes sean como de fabrica, como 
# en el ejemplo del obejto 'carro' este por default, tiene un largo, ancho, estado parado y 4 ruedas.

# Para especificar el estado inicial de un obejto perteneciente a una clase lo hacemos con un "CONSTRUCTOR"
# CONSTRUCTOR: Es un metodo especial que le da un estado inicial a los objetos. Forma de especificar claramente cual va hacer el estado incial de los objetos que pertenecen a una clase.

# Para definir un metodo constructor:


def __init__(self):     # Cuando escribes esto en python, estas definiendo que este va hacer tu constructor de tu clase. 
# Es el que le va a dar un estado iniciala los objetos que pertenecen a tu clase.
