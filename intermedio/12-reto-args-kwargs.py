def calculate_total(*products_and_prices, **options):
    """
    Calcula el total de una lista de productos y sus precios, con descuento opcional.
    
    Args:
        *products_and_prices: Tuplas de (producto, precio)
        **options: Argumentos con nombre (acepta 'discount' como porcentaje)
    
    Returns:
        tuple: (total final, diccionario con detalles de la compra)
        
    Raises:
        ValueError: Si los productos y precios no están correctamente emparejados
        ValueError: Si algún precio es negativo
    """
    # Validamos que los argumentos vengan en pares (producto, precio)
    if len(products_and_prices) % 2 != 0:
        raise ValueError("Cada producto debe tener su correspondiente precio")
    
    # Convertimos la lista de argumentos en pares de productos y precios
    products = products_and_prices[::2]
    prices = products_and_prices[1::2]
    
    # Validamos los precios
    for product, price in zip(products, prices):
        if not isinstance(price, (int, float)):
            raise ValueError(f"El precio de {product} debe ser un número")
        if price < 0:
            raise ValueError(f"El precio de {product} no puede ser negativo")
    
    # Creamos un diccionario de productos y precios
    purchase_details = dict(zip(products, prices))
    subtotal = sum(prices)
    
    # Aplicamos descuento si existe
    discount = options.get('discount', 0)
    if not isinstance(discount, (int, float)):
        raise ValueError("El descuento debe ser un número")
    if not 0 <= discount <= 100:
        raise ValueError("El descuento debe estar entre 0 y 100")
    
    # Calculamos el total con descuento
    discount_amount = subtotal * (discount / 100)
    total = subtotal - discount_amount
    
    # Agregamos información adicional al diccionario de detalles
    purchase_summary = {
        'products': purchase_details,
        'subtotal': subtotal,
        'discount_percentage': discount,
        'discount_amount': discount_amount,
        'total': total
    }
    
    return total, purchase_summary

# Ejemplo de uso
try:
    # Ejemplo básico
    total, details = calculate_total(
        "laptop", 1200,
        "mouse", 25.50,
        "keyboard", 50,
        discount=10
    )
    
    print(f"Total con descuento: ${total:.2f}")
    print("\nDetalles de la compra:")
    for product, price in details['products'].items():
        print(f"- {product}: ${price:.2f}")
    print(f"\nSubtotal: ${details['subtotal']:.2f}")
    print(f"Descuento ({details['discount_percentage']}%): ${details['discount_amount']:.2f}")
    print(f"Total final: ${details['total']:.2f}")
    
except ValueError as e:
    print(f"Error: {e}")