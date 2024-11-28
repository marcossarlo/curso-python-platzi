# Comprehension Lists en Python
# https://platzi.com/home/clases/10002-python/70970-comprehensions-lists-en-python/

# Una Comprehension List es una forma concisa de crear listas en Python, pues permite generar listas nuevas transformando cada elemento de una colección existente o creando elementos a partir de un rango. La sintaxis es compacta y directa, lo que facilita la comprensión del propósito de tu código de un vistazo.
# [expresión for elemento in iterable if condición]
# “Crea una nueva lista evaluando nueva_expresión para cada elemento en el iterable.”
# +info: https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions

# son una forma concisa de crear listas.
# son una forma de definir y crear listas en Python.
# son una forma de aplicar una operación a cada elemento de una lista.
# son una forma de aplicar una operación a cada elemento de un rango.
# son una forma de aplicar una operación a cada elemento de un iterable.
# son una forma de aplicar una operación a cada elemento de un diccionario.
# son una forma de aplicar una operación a cada elemento de un conjunto.

# hallar los cuadrados de los números del 1 al 10
squares = [x**2 for x in range(1, 11)]
print("Los cuadrados del 1 - 10:", squares)
cubes = [x**3 for x in range(1, 11)]
print("Los cubos del 1 - 10:", cubes)

# Transformar de Grados Celcius a Fahrenheit
print("\nTransformar de Grados Celcius a Fahrenheit")
celsius = [x*10 for x in range(1, 11)]
print("Grados Celcius:", celsius)
# Formula: F = (9/5 * C) + 32
fahrenheit = [(9/5 * temperature) + 32 for temperature in celsius]
print("Temperatura en Fahrenheit:", fahrenheit)

# Hayar los números pares de una lista
print("\nHayar los números pares de una lista")
numbers = [x for x in range(1, 21)]
print("Lista de números:", numbers)
even = [number for number in numbers if number % 2 == 0]
print("Números pares de la lista:", even)
odd = [number for number in numbers if number % 2 != 0]
print("Números impares de la lista:", odd)

# Crear una Transpuesta de una Matriz
print("\nCrear una Transpuesta de una Matriz")
matrix = [
    [1, 2, 3], 
    [4, 5, 6], 
    [7, 8, 9]
]
print("Matriz Original:", matrix)
transpose = [[row[i] for row in matrix] for i in range(len(matrix))]


# transpose = []
# for i in range(len(matrix)):
#     #print(i)
#     transpose_row = []
#     for row in matrix:
#         #print(row[i])
#         transpose_row.append(row[i])
#         print(transpose_row)
#     transpose.append(transpose_row)
#     print(transpose)
    
print("Matriz Transpuesta:", transpose)


