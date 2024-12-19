# Módulo: Métodos y estructura de clases en Python:
"""
Sistema de gestión de pedidos para un restaurante que utiliza métodos mágicos para manejar la representación, la comparación y las operaciones aritméticas de los pedidos. Además, aplicamos buenas prácticas para que sea Pythonic.

Caso real: Sistema de gestión de pedidos
Descripción del problema:
Cada pedido tiene un identificador, una lista de productos y un costo total.
Los pedidos se pueden combinar (sumar costos y productos).
Los pedidos deben ser comparables (por costo total).
Los pedidos deben tener una representación amigable y detallada.
"""

class Order:
    """
    Métodos mágicos utilizados:
        __init__: Inicializa los atributos del pedido.
        __str__: Devuelve una representación amigable (útil para usuarios).
        __repr__: Devuelve una representación técnica (útil para desarrolladores).
        __add__: Permite sumar pedidos combinando productos y costos.
        __eq__ y __lt__: Habilitan la comparación de pedidos.
    """
    TAX_RATE = 0.18  # Tasa de impuesto (18%)
    
    def __init__(self, order_id: int, products: list[str], total_cost: float):
        """Inicializa un pedido con un identificador, productos y costo total."""
        self.order_id = order_id
        self.products = products
        self.total_cost = total_cost

    def __repr__(self) -> str:
        """Representación oficial para depuración."""
        return f"Order(order_id={self.order_id}, products={self.products}, total_cost={self.total_cost:.2f})"

    def __str__(self) -> str:
        """Representación amigable para usuarios."""
        products_str = ", ".join(self.products)
        return f"Pedido #{self.order_id}: Productos: {products_str}. Total: ${self.total_cost:.2f}"

    def __add__(self, other: 'Order') -> 'Order':
        """Permite combinar dos pedidos sumando sus costos y productos."""
        combined_products = self.products + other.products
        combined_cost = self.total_cost + other.total_cost
        return Order(
            order_id=min(self.order_id, other.order_id),
            products=combined_products,
            total_cost=combined_cost
        )

    def __sub__(self, discount: float) -> 'Order':
        """Aplica un descuento al pedido y retorna un nuevo pedido con el descuento."""
        if discount < 0 or discount > self.total_cost:
            raise ValueError("El descuento debe ser mayor a 0 y menor o igual al total del pedido.")
        discounted_cost = self.total_cost - discount
        return Order(
            order_id=self.order_id,
            products=self.products,
            total_cost=discounted_cost
        )

    def __len__(self) -> int:
        """Devuelve el número de productos en el pedido."""
        return len(self.products)

    def __eq__(self, other: object) -> bool:
        """Compara dos pedidos según su costo total."""
        if not isinstance(other, Order):
            return NotImplemented
        return self.total_cost == other.total_cost

    def __lt__(self, other: 'Order') -> bool:
        """Ordena los pedidos según su costo total."""
        return self.total_cost < other.total_cost

    def apply_tax(self) -> 'Order':
        """Aplica el impuesto al total del pedido."""
        taxed_cost = self.total_cost * (1 + Order.TAX_RATE)
        return Order(
            order_id=self.order_id,
            products=self.products,
            total_cost=round(taxed_cost, 2)
        )

# Ejemplo de uso del sistema de pedidos
# Ejemplo de uso del sistema de pedidos extendido
if __name__ == "__main__":
    order1 = Order(order_id=1, products=["Pizza", "Refresco"], total_cost=20.50)
    order2 = Order(order_id=2, products=["Hamburguesa", "Papas"], total_cost=15.75)

    print("\nDetalle de los pedidos:")
    print(order1)  # Pedido #1: Productos: Pizza, Refresco. Total: $20.50
    print(order2)  # Pedido #2: Productos: Hamburguesa, Papas. Total: $15.75

    # Combinación de pedidos
    print("\nCombinación de pedidos:")
    combined_order = order1 + order2
    print(combined_order)  # Pedido #1: Productos: Pizza, Refresco, Hamburguesa, Papas. Total: $36.25

    # Aplicación de descuento
    print("\nAplicación de descuento:")
    discounted_order = combined_order - 5.00
    print(discounted_order)  # Pedido #1: Productos: Pizza, Refresco, Hamburguesa, Papas. Total: $31.25

    # Aplicación de impuestos
    print("\nAplicación de impuestos:")
    taxed_order = discounted_order.apply_tax()
    print(taxed_order)  # Pedido #1: Productos: Pizza, Refresco, Hamburguesa, Papas. Total: $36.88

    # Número de productos en un pedido
    print("\nNúmero de productos en el pedido:")
    print(len(combined_order))  # 4

    # Comparación de pedidos
    print("\nComparación de pedidos:")
    print(order1 > order2)  # True
    print(order1 == order2)  # False