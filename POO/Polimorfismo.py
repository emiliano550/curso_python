# POLIMORFISMO

class Coche():

    def desplazamiento(self):
        print('Me desplazo utilizando cuatro ruedas')

class Moto():

    def desplazamiento(self):
        print('Me desplazo utilizando dos ruedas ')

class Camion():

    def desplazamiento(self):
        print('Me desplazo utilizando seis ruedas')

#miVehiculo = Moto()
#miVehiculo.desplazamiento()

#miVehiculo2 = Coche()
#miVehiculo2.desplazamiento()

#miVehiculo3 = Camion()
#miVehiculo3.desplazamiento()



#POLIMORFISMO:
# Un objeto tiene la capacidad de cambiar de forma y de comportarse de diferente forma y dependiendo el contexto, se vera a que 'metodo' en este caso 'desplazamiento' tiene que llamar

def desplazamientovehiculo(vehiculo):
    vehiculo.desplazamiento()


#CREAMOS OBJETO de tipo camión
mivhehiculo = Moto()

#Utiizo el MÉTODO 'desplazamientovehiculo y le pasamos por parametro el OBJETO de tipo camión
desplazamientovehiculo(mivhehiculo)

#Cuando llamamos al MÉTODO 'desplazamientovehiculo', y pasamos por parametro el OBJETO 'miVehiculo' <-- este objeto se almacena en el parametro 'vehiculo' 
#y con el polimofismo, hace que se convierta en un OBJETO de tipo Camión y hace que llame al MÉTODO 'desplazamiento' de la clase camion


#En python se puede hacer de esta sencilla manera, porque es un lenguaje no tipado, osea que no se tienen que definir que tipo de valores utilizas
# En Java es mas complicado y se tiene que definir los valores 