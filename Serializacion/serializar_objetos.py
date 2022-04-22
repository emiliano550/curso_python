import pickle
#SERIALIZAR OBJETOS
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



#Metemos los objetos en una colección y serializar una colección de objetos
#Creamos los objetos
coche1 = Vehiculo('Mazda','MX5')
coche2 = Vehiculo('Seat','Leon')
coche3 = Vehiculo('Renault','Megane')

#Los metemos en una colección para serializarlos
coches =[coche1, coche2, coche3]

#Creamos una variable
fichero = open('loscoches', 'wb')

#1er argumento ---> nombre de la colección donde tenemos los objetos 'coches'....2do ---->nombre del fichero donde queremos voclar(guardar) esa información
pickle.dump(coches, fichero)
fichero.close()     # cerramos el fichero

#borramos el fichero de la memoria
del(fichero)



#ABRIMOS EL FICHERO
ficheroApertura = open('losCoches', 'rb')

#creamos una variable donde se va a guardar la informaión del fichero
misCoches = pickle.load(ficheroApertura)
ficheroApertura.close()

for c in misCoches:
    print(c.estado())