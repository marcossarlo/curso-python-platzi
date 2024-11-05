# MODÚLO: Funciones y Manejo de Excepciones en PytHON
# CLASE: ¿Cómo realizar una función recursiva en Python?
# https://platzi.com/home/clases/10002-python/70191-recursividad/

# ¿Cómo realizar una función recursiva en Python?
# La recursividad es un concepto en programación que se refiere a la capacidad de una función de llamarse a sí misma.
# Una función recursiva es una función que se llama a sí misma dentro de su definición.
# La recursividad se utiliza para resolver problemas que pueden dividirse en subproblemas más pequeños.
# Un problema recursivo tiene dos partes: el caso base y el caso recursivo.

# El caso base es la condición que detiene la recursión.
# El caso recursivo es la llamada a la función dentro de la función.
# La recursividad se utiliza para resolver problemas de manera más sencilla y elegante.
# La recursividad es una técnica poderosa que se utiliza en programación para resolver problemas de manera eficiente.
# La recursividad se utiliza en algoritmos de búsqueda, ordenación y optimización.
# La recursividad se utiliza en algoritmos de backtracking y divide y vencerás.
# La recursividad se utiliza en algoritmos de programación dinámica y memoización.
# La recursividad se utiliza en algoritmos de grafos y árboles.
# La recursividad se utiliza en algoritmos de inteligencia artificial y aprendizaje automático.

# Ejemplo: Factorial de un número
# El caso base es el factorial de 0, que es 1.
# El caso recursivo es el factorial de un número n, que es n * factorial(n-1).

## Mi código
# def factorial(n):
# 	if n == 0:
# 		return 1
# 	elif n < 0:
# 		return "No existe el factorial de un número negativo"
# 	else:
# 		return n * factorial(n-1)

# number = int(input("Ingresa un número: "))
# print("Factorial de", number)
# print(factorial(number))

## Código de Copilot:
def factorial(n):
    if n < 0:
        return "No existe el factorial de un número negativo"
    elif n == 0:
        return 1
    else:
        return n * factorial(n - 1)

try:
    number = int(input("Ingresa un número: "))
    print(f"Factorial de {number} es: {factorial(number)}")
except ValueError:
    print("Por favor, ingresa un número entero válido.")


