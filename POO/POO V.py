class Coche():                #clase  
  
    def __init__(self):      # Metodo constructor   

        self.__largoChasis = 250    # propiedades
        self.__anchoChasis=120
        self.__ruedas = 4          #ENCAPSULAMIENTO de la variable 'ruedas'     
        self.__enmarcha=False

    def arrancar(self, arrancamos):     #Método arrancar  
        self.__enmarcha= arrancamos  

        if self.__enmarcha:
            chequeo = self.__chequeo_interno() 

        if self.__enmarcha and chequeo:
            return 'El coche esta en marcha'
        
        elif self.__enmarcha and chequeo == False:
            return 'Algo ha ido ma en el chequeo, no podemos arrancar'

        else:
            return 'El coche esta parado'


    def estado(self):                    #Método estadp       
        print('El coche tiene ', self.__ruedas, 'ruedas. Un ancho de ', self.__anchoChasis, 'y un largo de ', self.__largoChasis)
       

    def __chequeo_interno(self):              # Nuevo método - ENCAPSULADO
        print('Realizando chequeo interno')

        self.gasolina = 'ok'                 # creando variables del metodo       
        self.aceite = 'ok'
        self.puertas = 'cerradas'

        if self.gasolina == 'ok' and self.aceite == 'ok' and self.puertas =='cerradas':
            return True
        else:
            return False


miCoche=Coche()             
print(miCoche.arrancar(True)) 
miCoche.estado()
#print(miCoche.chequeo_interno())

print('-------------A continuación creamos el segundo objeto-------------')

miCoche2 = Coche()
print(miCoche2.arrancar(False))  
miCoche2.estado()



# ENCAPSULACIÓN DE METODOS
# Para encapsular un método se pone doble guion bajo (__) antes del nombre del método y de igual forma si queremos llamar este método se tiene que escribir igual

