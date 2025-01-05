def add(a: float, b: float) -> float:
    """Suma dos números."""
    return a + b

def subtract(a: float, b: float) -> float:
    """Resta dos números."""
    return a - b

if __name__ == "__main__":
    # Código de prueba
    print("Pruebas rápidas de la calculadora:")
    print(f"5 + 3 = {add(5, 3)}")
    print(f"10 - 7 = {subtract(10, 7)}")


# La construcción if __name__ == "__main__": es una característica fundamental en Python para controlar la ejecución de un script y definir su comportamiento dependiendo de cómo se use (directamente o como módulo importado).

# Ejemplo de uso como módulo

# import calculator:
# print("Uso del módulo 'calculator':")
# print(f"8 + 4 = {calculator.add(8, 4)}")
# print(f"9 - 2 = {calculator.subtract(9, 2)}")
