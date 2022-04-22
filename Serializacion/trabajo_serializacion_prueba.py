import pickle

# creamos un fichero en memoria
#utilizamos el 1er argumento del fichero que queremos abrir y el 2do el 'rb' read binary
fichero=open('lista_nombres', 'rb')

#La información del fichero la guardamos en esta varibale
#Utilizamos el método 'load' para cargar la información que tenemos guardada en 'fichero'
lista = pickle.load(fichero)
print(lista) #Estamos accediento a la lista del fichero externo binario
