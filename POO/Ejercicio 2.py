class Persona():

#Método CONSTRUCTOR y PARAMETROS que le dan el estado inicial
    def __init__(self,nombre, apellido, edad, genero, ciudad, pais):

        self.nombre = nombre 
        self.apellido = apellido
        self.edad = edad
        self.genero = genero
        self.ciudad = ciudad 
        self.pais = pais

    def descripcion(self):
        print('Nombre: ', self.nombre, '\nApellido: ', self.apellido, '\nEdad: ', self.edad, '\nGenero: ', self.genero, '\nCiudad: ', self.ciudad, '\nPais: ', self.pais)

class Experiencia(Persona):

    def __init__(self, anterior_puesto, empresa_anterior, anios, sueldo_anterior, nombre, apellido, edad, genero, ciudad, pais):
        super().__init__(nombre, apellido, edad, genero, ciudad, pais)

        self.anterior_puesto = anterior_puesto
        self.empresa_anterior = empresa_anterior
        self.anios = anios
        self.sueldo_anterior = sueldo_anterior


    def descripcion(self):
        super().descripcion()
        print('Anterior Puesto: ', self.anterior_puesto, '\nEmpresa anterior: ', self.empresa_anterior, '\nAños: ', self.anios, '\nSueldo Anterior: ', self.sueldo_anterior)

class Empleo_nuevo(Experiencia):
    
    def __init__(self, nuevo_puesto, nombre_empresa, area, sueldo_actual, anterior_puesto, empresa_anterior, anios, sueldo_anterior, nombre, apellido, edad, genero, ciudad, pais):
        super().__init__(anterior_puesto, empresa_anterior, anios, sueldo_anterior, nombre, apellido, edad, genero, ciudad, pais)

        self.nuevo_puesto = nuevo_puesto
        self.nombre_empresa = nombre_empresa
        self.area = area
        self.sueldo_actual = sueldo_actual

    def descripcion(self):
        super().descripcion() 
        print('Nuevo puesto: ',self.nuevo_puesto, '\nNombre de Nueva empresa: ', self.nombre_empresa, '\nÁrea: ', self.area, '\nSueldo Actual: ', self.sueldo_actual, '\n')


#CREAMOS NUESTRO OBJETO:
Posicion = Empleo_nuevo('Intern Marketing and Operations', 'Microsoft', 'Marketing', '$4,3000', 'IT Trainee', 'TCS', '8 meses', '$11,000', 'Abraham', 'Márquez', '26 años', 'Masculino', 'CDMX', 'México')
Posicion.descripcion()

Posicion2 =Empleo_nuevo('Abogado', 'SICT', 'Caminos Rurales', '$15,000', 'Abogado Jr', 'SCT', '2', '$10,000', 'Carlos', 'Márquez', '24 años', 'Masculino', 'CDMX', 'México')
Posicion2.descripcion()

  
