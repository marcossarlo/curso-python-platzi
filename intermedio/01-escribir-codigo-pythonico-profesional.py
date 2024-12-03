# ver las directrices generales escribiendo:
#import this

# 1. Uso de List Comprehensions
print("1. Uso de List Comprehensions:")
# No Pythonico
nueva_lista = []
for x in range(10):
    nueva_lista.append(x * 2)
print(f"No Pythonico: {nueva_lista}")

# Pythonico
new_list = [x * 2 for x in range(10)]
print(f"Pythonico: {new_list}")

# 2. Desempaquetado de Variables
print("\n2. Desempaquetado de Variables:")
# No Pythonico
punto = (3, 5)
x = punto[0]
y = punto[1]

# Pythonico
x, y = punto
print(x, y)

# 3. Uso de enumerate() y zip()
print("\n3. Uso de enumerate() y zip()")
print("Evita manejar índices manualmente y trabaja con múltiples iterables.")
# No Pythonico
for i in range(len(new_list)):
    #print(i, new_list[i])
    continue
# Pythonico
for i, value in enumerate(new_list):
    print(i, value)

# Ejemplo de uso de zip()
print("Ejemplo de uso de zip()")
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']

# No Pythonico
for i in range(len(list1)):
    #print(list1[i], list2[i])
    continue

# Pythonico
for item1, item2 in zip(list1, list2):
    print(item1, item2)

# 4. Uso de Generadores
print("\n4. Uso de Generadores")
print("Los generadores son más eficientes en memoria que las listas, especialmente con grandes cantidades de datos.")
# Lista (usa más memoria)
numeros = [x * 2 for x in range(10)]
# Generador (usa menos memoria)
numeros_gen = (x * 2 for x in range(10))

# 5. Manejo de Excepciones en Lugar de Condicionales
print("\n5. Manejo de Excepciones en Lugar de Condicionales:\n Python prefiere el enfoque EAFP (Easier to Ask for Forgiveness than Permission).")
# No Pythonico (comprobación explícita)
"""
if 'clave' in diccionario:
    valor = diccionario['clave']

# Pythonico (manejo de excepciones)
try:
    valor = diccionario['clave']
except KeyError:
    valor = None
"""

# Ejemplo de Código Pythonico y Profesional
print("\nEjemplo de Código Pythonico y Profesional")
from typing import List

def calcular_promedio(numeros: List[int]) -> float:
    """Calcula y devuelve el promedio de una lista de números enteros."""
    if not numeros:
        raise ValueError("La lista no puede estar vacía.")
    
    total = sum(numeros)
    return total / len(numeros)

numeros = [10, 20, 30, 40]
print(f"El promedio es: {calcular_promedio(numeros):.2f}")


