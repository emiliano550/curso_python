class Persona():

#Método CONSTRUCTOR y PARAMETROS que le dan el estado inicial
    def __init__(self, nombre, apellido, edad, genero, ciudad, pais): 
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad 
        self.genero = genero
        self.ciudad = ciudad
        self.pais = pais 

#Método 
    def descripcion(self):
        print('Nombre: ', self.nombre, 'Apellido: ', self.apellido, 'Edad: ', self.edad, 'Genero: ', self.genero, 'Ciudad: ',self.ciudad, 'Pais: ', self.pais)


class Alumno(Persona):

    def __init__(self, universidad, carrera, turno, no_cuenta, promedio, nombre, apellido, edad, genero, ciudad, pais):
        super().__init__(nombre, apellido, edad, genero, ciudad, pais)

        self.universidad = universidad
        self.carrera = carrera
        self.turno = turno
        self.no_cuenta = no_cuenta
        self.promedio = promedio

#Método
    def descripcion(self):
        super().descripcion()
        print('Universidad: ', self.universidad, 'Carrera: ', self.carrera, 'Turno: ', self.turno, 'No. Cuenta: ', self.no_cuenta, 'Promedio: ', self.promedio)


Emiliano = Alumno('UNITEC', 'Ingeniería Mecatrónica', 'Vespertino', '14002261', '8.1', 'Emiliano', 'Márquez', '22', 'Masculino', 'CDMX', 'México')
Emiliano.descripcion() # descripción de la clase Alumno, que tambien hereda los atributos y metodos de la clase Padre que es Persona

Carlos = Alumno('CUGS', 'Licenciatura en Derecho', 'Matutino', '14886547', '7.5', 'Carlos', 'Márquez', '23', 'Masculino', 'GDL', 'Nezahualcoyotl')
Carlos.descripcion()

Esteban = Alumno('UNIVER', 'Licenciatura en Derecho', 'Vespertino', '12476947', '7.0', 'Esteban', 'Mora', '29', 'Masculino', 'Zapopan', 'Jalisco')
Esteban.descripcion()


