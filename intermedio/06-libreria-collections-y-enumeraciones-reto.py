"""
Reto:
Implementa un sistema de gestión de pedidos, utilizando Colecciones y Enumeraciones
1º defaultdict: para llevar registro de cada uno de los productos que se tienen
2º enumeracion: para saber el estado de una orden: Pendiente, enviado, entregado
3º contador: para llevar el conteo de cada uno de los productos
"""

from collections import defaultdict, Counter
from enum import Enum, auto

# Enumeración para los estados de las órdenes
class OrderStatus(Enum):
    PENDING = 1
    SHIPPED = 2
    DELIVERED =3

# Registro de productos con defaultdict
products_inventory = defaultdict(int)

# Contador para llevar el registro total de productos en pedidos
product_counter = Counter()

# Función para añadir productos al inventario
def add_product_to_inventory(product_name, quantity):
    products_inventory[product_name] += quantity
    print(f"Producto añadido: {product_name}, cantidad actual: {products_inventory[product_name]}")

# Clase para representar una orden
class Order:
    def __init__(self, order_id):
        self.order_id = order_id
        self.items = defaultdict(int)
        self.status = OrderStatus.PENDING

    def add_item(self, product_name, quantity):
        if products_inventory[product_name] >= quantity:
            self.items[product_name] += quantity
            products_inventory[product_name] -= quantity
            product_counter[product_name] += quantity
            print(f"Producto añadido a la orden {self.order_id}: {product_name}, cantidad: {quantity}")
        else:
            print(f"Stock insuficiente para {product_name}. Disponibles: {products_inventory[product_name]}")

    def change_status(self, status):
        self.status = status
        if self.status == OrderStatus.PENDING:
            new_status = "Pendiente"
        elif self.status == OrderStatus.SHIPPED:
            new_status = "Enviado"
        elif self.status == OrderStatus.DELIVERED:
            new_status = "Entregado"
            

        print(f"Estado de la orden {self.order_id} actualizado a: {new_status}")

# Crear inventario inicial
print("Crear inventario inicial:")
add_product_to_inventory("Laptop", 10)
add_product_to_inventory("Mouse", 50)
add_product_to_inventory("Teclado", 30)
print("Inventario actual:", dict(products_inventory))

# Crear y gestionar una orden
print("\nCrear y gestionar una orden:")
order_1 = Order(order_id=1)
order_1.add_item("Laptop", 2)
order_1.add_item("Mouse", 5)

order_2 = Order(order_id=2)
order_2.add_item("Teclado", 3)
order_2.add_item("Mouse", 10)

# Cambiar estado de la orden
print("\nCambiar estado de la orden:")
order_1.change_status(OrderStatus.DELIVERED)
order_2.change_status(OrderStatus.SHIPPED)

# Mostrar conteo de productos en pedidos
print("\nMostrar conteo de productos en pedidos:")
print("Conteo de productos en pedidos:", product_counter)

# Mostrar inventario restante
print("\nMostrar inventario restante:")
print("Inventario restante:", dict(products_inventory))
