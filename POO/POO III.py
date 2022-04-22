class Coche():           #clase  
    largoChasis = 250    # propiedades
    anchoChasis=120
    ruedas = 4
    enmarcha=False

                               #Caracteristicas de un metodo(comportamiento): def, nombre de la función, parametro por defecto llamado 'self(objeto perteneciente a la clase o instancia perteneciente a la clase)',pass 
    def arrancar(self):        #Los metodos se definen de esta forma, porque son una función que pertenecen a una clase. Y las funciones normales no pertenecen a una clase.
        self.enmarcha = True   #self es = a el objeto que en este caso es 'miCoche'
    
    def estado(self):
        if self.enmarcha:
            return 'El coche esta en marcha'
        else:
            return 'El coche esta parado'

miCoche=Coche()              #Definimos nuestro objeto y el nombre de la clase a la que pertenece el objeto/instancia. INSTANCIAR UNA CLASE 
print('El largo de mi coche es: ',miCoche.largoChasis)
print('El coche tiene', miCoche.ruedas)
#miCoche.arrancar()

print(miCoche.estado())

# NOTA: Tenemos 4 propiedades en nuestra clase, y 2 comportamientos(metodos)