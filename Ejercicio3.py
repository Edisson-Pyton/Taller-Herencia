class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

class Carro(Vehiculo):
    def __init__(self, marca, modelo, numero_de_puertas):
        super().__init__(marca, modelo)
        self.numero_de_puertas = numero_de_puertas

class Moto(Vehiculo):
    def __init__(self, marca, modelo, tipo_de_motor):
        super().__init__(marca, modelo)
        self.tipo_de_motor = tipo_de_motor

carro = Carro("Lamborghini", "Urus", 5)
moto = Moto("Honda", "Hornet 600", "tetracilindrico")

print(f"Carro: Marca={carro.marca}, Modelo={carro.modelo}, Puertas={carro.numero_de_puertas}")
print(f"Moto: Marca={moto.marca}, Modelo={moto.modelo}, Motor={moto.tipo_de_motor}")
