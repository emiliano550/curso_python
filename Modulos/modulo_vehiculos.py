# HERENCIA

#Sobre escritura de métodos
#Herencia simple y múltiple
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


class Furgoneta(Vehiculo):

    def carga(self, cargar):
        self.cargado = cargar
        if self.cargado:
            return 'La furgoneta está cargada'
        else:
            return 'La furgoneta no está cargada'


# Crearemos los OBJETOS para que HEREDE todas las propiedas de la clase Vehivulo
#Al colocar en los parentesis 'Vehiculo' la clase/objeto 'Moto' hereda en automatico todas las propiedades(varibales), de la clase vehiculo
# Se va a heredar todo, incluyendo el CONSTRUCTOR
class Moto(Vehiculo):    
    hcaballito = ''
    def caballito(self):
        self.hcaballito ='Voy haciendo el caballito'

#Esta clase, no hereda nada de otras, es una clase independiente
class VElectricos(Vehiculo):
    def __init__(self, marca, modelo):   
        super(). __init__(marca, modelo)              #CONSTRUCTOR
        self.autonomia = 100

    def cargarEnergia(self):
        self.cargando = True



#SOBRE ESCRITURA DE MÉTODOS:
#Se tiene que escribir de nuevo el método estado con las mismas variables del metodo herdado, porque lo va a sobreescribir
    def estado(self):
        print('Marca: ', self.marca, '\nModelo: ', self.modelo, '\nEn Marcha: ',
        self.enmarcha, '\nAcelerando: ', self.acelera, '\nFrenando: ', self.frena, '\n',self.hcaballito)
    








