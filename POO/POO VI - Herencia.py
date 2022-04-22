#clase padre
class Vehiculo():     

#CONSTRUCTOR con sus parametros
    def __init__(self, marca, modelo):        
        self.marca = marca 
        self.modelo = modelo 
        self.enmarcha = False
        self.acelera = False
        self.frena = False

# Métodos o comportamiento de tipo vehiculo        
    def arrancar(self):
        self.enmarcha = True

    def acelerar(self):
        self.acelera = True

    def frenar(self):
        self.frena = True

    def estado(self):
        print('Marca: ', self.marca, '\nModelo: ', self.modelo, '\nEn Marcha: ',
        self.enmarcha, '\nAcelerando: ', self.acelera, '\nFrenando: ', self.frena)



# Crearemos los OBJETOS para que HEREDE todas las propiedas de la clase Vehivulo
#Al colocar en los parentesis 'Vehiculo' la clase/objeto 'Moto' hereda en automatico todas las propiedades(varibales), de la clase vehiculo
# Se va a heredar todo, incluyendo el CONSTRUCTOR
class Moto(Vehiculo):    
    pass
miMoto = Moto('Honda', 'CBR')

miMoto.estado()

    


























# HERENCIA

# ¿QUÉ ES LA HERENCIA?
# Para reutilizar código en caso de crear objetos similares

# ¿Qué carcaterísticas en común tienen todos los objetos?
#Ejemplo: *Marca *Modelo

# ¿Qué carcaterísticas en común tienen todos los objetos?
#Ejemplo van hacer capaces de: *Arrancar  *Acelerar    *Frenar

#CLASE PADRE O SUPER CLASE: 