# Ejercicio 2
# Implementar la clase producto (id, titulo, precio)
# Implementar un carrito de la compra (clase CarritoCompra)
# Las funcionalidades del carrito tienen que ser:
# - añadir producto (si se añade un producto con cantidad 0, se elimina del carrito)
# - quitar producto
# - mostrar precio total €
# - pagar compra (son 2 acciones, la de mostrar el ticket y luego vaciar el carrito)

class Producto:
    def __init__(self, producto_id, titulo, precio):
        self.id = producto_id
        self.titulo = titulo
        self.precio = precio

    def __str__(self):
        return f"Producto id={self.id}, titulo={self.titulo}, precio={self.precio}"

    def __repr__(self):
        return self.__str__()

class ProductoEnCarrito(Producto):
    def __init__(self, producto, cantidad):
        super().__init__(producto.id, producto.titulo, producto.precio)
        self.cantidad = cantidad

    def __str__(self):
        return super().__str__(self) + f", cantidad={self.cantidad}"

    def __repr__(self):
        return self.__str__()


class CarritoCompra:
    def __init__(self):
        self.carrito = {}

    def add_producto(self, producto, cantidad=1):
        if producto.id not in self.carrito:
            if not cantidad:
                return
            self.carrito[producto.id] = ProductoEnCarrito(producto, cantidad)
            return

        if cantidad <= 0:
            self.delete_producto(producto.id)
            return

        self.carrito[producto.id].cantidad += cantidad


    def delete_producto(self, producto_id, cantidad=0):
        if producto_id in self.carrito and not cantidad:
            del self.carrito[producto_id]
            return

        self.carrito[producto_id].cantidad -= cantidad


    # Calcular el precio total al ir añadiendo/eliminando productos del carrito
    # así no recorremos 2 veces el carrito para sacar el total (una en este método
    # y la otra en el __str__)
    def get_precio_total(self):
        total_compra = 0
        for producto in self.carrito.values():
            total_compra += producto.precio * producto.cantidad
        return total_compra

    def vaciar_carrito(self):
        self.carrito = {}

    def mostrar_ticket_compra(self):
        print(self.carrito)

    def pagar(self):
        self.mostrar_ticket_compra()
        self.vaciar_carrito()

    def __str__(self):
        ticket = "Ticket de la compra\n\n"
        total_compra = 0
        for producto in self.carrito.values():
            ticket += (f"{producto.titulo:<15} - {producto.precio:8.2f}€ x {producto.cantidad:2} = "
                       f"{(producto.precio * producto.cantidad):8.2f}€\n")
            total_compra += producto.precio * producto.cantidad

        ticket += f"Total: {total_compra:36}€"
        return ticket



producto1 = Producto(1, "Auriculares", 28.99)
producto2 = Producto(2, "Chicles", 1.70)

cesta = CarritoCompra()

cesta.add_producto(producto1, 0)
print(cesta)

cesta.add_producto(producto1)
cesta.add_producto(producto1, 2)
cesta.add_producto(producto2, 5)
print(cesta)

cesta.add_producto(producto2, 0)
print(cesta)

cesta.add_producto(producto2, 5)

cesta.delete_producto(producto2.id, 2)
# cesta.add_producto(producto2, -2)

print(cesta)