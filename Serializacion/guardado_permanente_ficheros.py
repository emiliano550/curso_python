import pickle
#GUARDAR DATOS DE FORMA PERMANENTE EN FICHEROS

#creamos la clase para hacer objetos de tipo persona
class Persona:

#creamos el constructor con 3 parametros
    def __init__(self, nombre, genero, edad):
        self.nombre = nombre
        self.genero = genero
        self.edad = edad
        print('Se ha creado una persona nueva con el nombre de ', self.nombre)

#Utilizamos el método especial str ----> Para convertir en cadena de texto la información de un objeto 
    def __str__(self):
        return '{} {} {}'.format(self.nombre, self.genero, self.edad)
    
# Creamos clase 
class ListaPersonas:

    personas=[]  #Creamos lista para grabar y para leer 

    def __init__(self):
        listaDePersonas = open('ficheroExterno', 'ab+')
        listaDePersonas.seek(0)

        try:
            self.personas=pickle.load(listaDePersonas)
            print('Se cargaron {} personas del fichero externo'.format(len(self.personas)))
        except: 
            print('El fichero esta vacio') 
        finally:
            listaDePersonas.close()
            del (listaDePersonas)

#Creamos dos métodos----> 1ro para agregar a las personas a esa lista y 2do-----> para leer a las personas que esten guardadas en esta lista
#1er Método 
    def agregarPersonas(self, p):
        self.personas.append(p)     #Utilizamos el método 'append' para que la persona sea agregada a la lista 'personas'
        self.guardarPersonasEnFicheroExterno()

#2do Método, mostrara la información guardada en la lista
    def mostrarPersonas(self):
        for p in self.personas:     #utilizamos un ciclo for para recorrer la lista de personas y en cada vuelta del bucle, nos ira imprimiendo cada persona en us interior
            print(p)

    def guardarPersonasEnFicheroExterno(self):
        listaDePersonas=open('ficheroExterno', 'wb')
        pickle.dump(self.personas, listaDePersonas)
        listaDePersonas.close()
        del(listaDePersonas)

    def mostrarInfoFicheroExterno(self):
        print('La infromación del fichero externo es la siguiente: ')
        for p in self.personas:
            print(p)

#Creamos un objeto de tipo 'ListaPersonas' para poder utilizar el metodo --->'agregarPersonas' y el método--->'mostrar Personas'
miLista =ListaPersonas()
persona =Persona('Ana', 'Femenino', 19)
miLista.agregarPersonas(persona)
miLista.mostrarInfoFicheroExterno()


#p = Persona('Sandra','Femenino', 2)        #creamos el primer objeto de la clase 'Persona'
#miLista.agregarPersonas(p)  #utilizamos el objeto 'miLista' para agregar esta personas a la lista

#miLista= ListaPersonas()
#p = Persona('Antonio','Maasculino',39)
#miLista.agregarPersonas(p)

#miLista= ListaPersonas()
#p = Persona('Ana','Femenino', 19)
#miLista.agregarPersonas(p)

# utilizamos el objeto mi lista para mostrar las personas
#miLista.mostrarPersonas()