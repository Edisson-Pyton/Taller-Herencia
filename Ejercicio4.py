class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

class Empleado(Persona):
    def __init__(self, nombre):
        super().__init__(nombre)

    def trabajar(self):
        print(f"{self.nombre} anda trabajando.")

class Deportista(Persona):
    def __init__(self, nombre):
        super().__init__(nombre)

    def entrenar(self):
        print(f"{self.nombre} anda entrenando.")

class EmpleadoDeportista(Empleado, Deportista):
    def __init__(self, nombre):
        super().__init__(nombre)

persona1 = EmpleadoDeportista("Nicolas")
persona1.trabajar()
persona1.entrenar()

print(EmpleadoDeportista.__mro__)
