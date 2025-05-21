class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

class ProductoPerecedero(Producto):
    def __init__(self, nombre, precio, fecha_vencimiento):
        super().__init__(nombre, precio)
        self.fecha_vencimiento = fecha_vencimiento

producto = ProductoPerecedero("Queso", 5500, "2026-05-25") 
print(f"Nombre: {producto.nombre}")
print(f"Precio: ${producto.precio}")
print(f"Fecha de vencimiento: {producto.fecha_vencimiento}")
