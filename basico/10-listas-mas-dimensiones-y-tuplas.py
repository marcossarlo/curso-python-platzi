# Listas de más dimensiones y Tuplas
# https://platzi.com/home/clases/10002-python/70088-listas-de-mas-dimensiones-y-tuplas/

# MATRICES: 
# Una matriz es una colección de elementos ordenados que se organiza en filas y columnas. Se pueden representar con listas anidadas.
# Las matrices en Python son una herramienta poderosa que permite organizar datos en listas de listas, facilitando su manejo y manipulación.

# TUPLA:
# Una tupla es una colección de elementos ordenados que no se pueden modificar. Se definen con paréntesis y los elementos se separan por comas.

# Las tuplas se utilizan para proteger los datos que no deben ser modificados.

# Las tuplas son más rápidas y ocupan menos espacio que las listas.
# Las tuplas se utilizan para proteger los datos que no deben ser modificados.
# Las tuplas son inmutables, es decir, no se pueden modificar después de su creación.
# Las tuplas pueden contener cualquier tipo de dato.
# Las tuplas se pueden anidar, es decir, podemos tener tuplas de tuplas.
# Las tuplas se pueden utilizar como claves en un diccionario, mientras que las listas no.
# Las tuplas pueden ser retornadas por una función.
# Las tuplas son iterables.
# Las tuplas son más seguras que las listas.    

# Listas de varias dimensiones
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix)
print(matrix[1][2])

# Crea un tablero self.board de 10x10, representado por una lista de listas, inicializado con espacios en blanco ' '.
print("\nTablero:")
board = [[' ' for _ in range(10)] for _ in range(10)]
print(board)
#print(len(board[0]))

# Tuplas
print('\nTuplas')
number = (1, 2, 3, 4, 5) 
    # number = 1, 2, 3, 4, 5
print(type(number), number)
print(number[1])
#number[0] = 10
# print(number) # Error: 'tuple' object does not support item assignment

# Incluir Listas dentro de las Tuplas
print('Incluir Listas dentro de las Tuplas')
numbers = (1, 2, 3, ['a', 'b', 'c'])
print(type(numbers), numbers)
print(numbers[3])
print(numbers[3][2])
print('Agregar un elemento a la lista que está dentro de la Tupla')
print(numbers)
numbers[3].append('d')
print(numbers)










