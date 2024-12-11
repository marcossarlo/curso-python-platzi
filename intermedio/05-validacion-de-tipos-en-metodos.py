# Validación de tipos en métodos
# https://platzi.com/home/clases/10002-python/71733-validacion-de-tipos-en-metodos/
"""
Validación de Tipos en Métodos en Python:
La validación de tipos en métodos es el proceso de verificar que los parámetros y valores retornados cumplan con los tipos esperados, asegurando que el código sea más robusto, legible y menos propenso a errores. Aunque Python es un lenguaje dinámico, donde los tipos no son estrictos en tiempo de ejecución, se pueden implementar validaciones explícitas o usar herramientas para garantizar la consistencia de los tipos.
"""
from typing import Union

def divide(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Los parámetros deben ser enteros o flotantes.")
    if b == 0:
        raise ZeroDivisionError("El divisor NO puede ser 0")
    
    return a/b
try:
    div_1 = divide(45.8,12.50)
    print(f"Resultado: {div_1}")
except (ZeroDivisionError, TypeError, Exception) as e:
    print(e)

    


    