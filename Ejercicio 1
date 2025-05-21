class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")

class Estudiante(Persona):
    def __init__(self, nombre, edad, programa):
        super().__init__(nombre, edad)  
        self.programa = programa

    def presentarse(self):
        super().presentarse()  # Usamos el método de la clase base
        print(f"Estudio el programa de {self.programa}.")

estudiante1 = Estudiante("Luis", 23, "Enfermeria")
estudiante1.presentarse()
