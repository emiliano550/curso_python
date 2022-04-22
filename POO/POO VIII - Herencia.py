class Persona():

# Método constructor y Parametros que le dan un estado inicial
    def __init__(self, nombre, edad, Lugar_residencia):        
        self.nombre = nombre                                                #Variables de la clase
        self.edad = edad
        self.lugar_residencia = Lugar_residencia

#Método
    def descripcion(self):
        print('Nombre: ', self.nombre, 'Edad: ', self.edad, 'Residencia: ', self.lugar_residencia)


class Empleado(Persona):  #Con HERENCIA, le hereda todas las variables de la clase 'PERSONAS' a esta clase 'EMPLEADO'

 # Método constructor y Parametros 
    def __init__(self, salario, antiguedad, nombre_empleado, edad_empleado, residencia_empleado):

#Colocamos la función 'super' dentro del Constructor, y esta esta llamando al 'MÉTODO __init__' de la CLASE PADRE, donde se almacenara nombre, edad, lugar...y aqui almacenaremos los valores
        super().__init__ (nombre_empleado, edad_empleado, residencia_empleado)

        self.salario = salario
        self.antiguedad = antiguedad

    def descripcion(self):
        super().descripcion()
        print('Salario: ', self.salario, 'Antiguedad: ', self.antiguedad)

# Creación de los OBJETOS
#Como estamos llamando al constructor le pasamos los Argumentos: nombre, edad, luga....
Manuel = Empleado(1500, 15, 'Manuel', 55, 'Colombia')  

#Ahora llamamos al método 'descripción' para imprimir esas propiedades
Manuel.descripcion()
print(isinstance(Manuel, Persona))
 
# PRINCIPIO DE SUSTITUCIÓN
# 'Es siempre un/a': en este caso la clase 'Empleado', no puede ser sin la clase 'Persona', porque no puede ser primero que la otra.
#Función 'isinstance()': Para saber si un OBJETO es instancia de una clase determinada. Para saber si un objeto pertenece a una clase o no.
# La función isinstance(), devuelve 'True', si pertenece a una clase. Y devuelve 'False', sino pertenece.





















# HERENCIA 

#FUNCIÓN super(): Va a llamar al método de la clase padre

#ISINSTANCE()

