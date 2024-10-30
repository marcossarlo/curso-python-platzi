# MODÚLO: Funciones y Manejo de Excepciones en PytHON
# CLASE: Funciones Lambda y Programación Funcional en Python
# https://platzi.com/home/clases/10002-python/70190-funciones-lambda-y-programacion-funcional/

# que hace lambda?
# lambda es una palabra clave en Python que se utiliza para definir funciones anónimas.
# Las funciones anónimas son funciones que no tienen un nombre.
# Las funciones anónimas se crean con la palabra clave lambda seguida de los argumentos de la función, dos puntos y la expresión que se evaluará.
# Las funciones anónimas se utilizan para crear funciones simples y pequeñas que se utilizan una sola vez.
add = lambda a, b: a + b
print("Suma:", add(4,18))

multiply = lambda a, b: a * b
print("Multiplicación:", multiply(4,18))

# Cuadrado de cada número
square = lambda x: x * x
print("Cuadrado de un número:", square(4))

# Cuadrado de cada número en una lista
numbers = range(11)
print(numbers)
# list() convierte un iterable en una lista.
# map() es una función que toma dos argumentos: una función y una secuencia iterable.
# map() aplica la función a cada elemento de la secuencia iterable.
squared_numbers = list(map(lambda x: x * x, numbers))
print("\n")
print("Cuadrado de cada número en una lista:")
print(squared_numbers)

#ejemplos de map()
# Obtener la longitud de cada palabra en una lista
words = ['manzana', 'arandano','banana', 'cereza', 'uva', 'pera']
print("\n")
print("Longitud de cada palabra en una lista:")
print(words)
length_words = list(map(lambda x: len(x), words))
print(length_words)

# Obtener números pares
# filter()?
# es una función que toma dos argumentos: una función y una secuencia iterable.
# aplica la función a cada elemento de la secuencia iterable y devuelve un iterador con los elementos que cumplen la condición.
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("\n")
print("Números pares de una lista:")
print(even_numbers)

# Ordenar una lista de tuplas por el segundo elemento de cada tupla
tuples = [(1, 2), (4, 1), (13, -3), (9, 10)]
print("\n")
print("Ordenar una lista de tuplas por el segundo elemento de cada tupla:")
print(tuples)
# sorted() ordena una secuencia iterable.
# key es un argumento opcional que toma una función que se aplica a cada elemento de la secuencia iterable antes de ordenar.
sorted_tuples = sorted(tuples, key=lambda x: x[1])
print(sorted_tuples)

# Ordenar una lista de diccionarios por el valor de una clave
people = [
    {"name": "Marcos", "age": 25},
    {"name": "Sarlo", "age": 30},
    {"name": "Juan", "age": 20}
]
print("\n")
print("Ordenar una lista de diccionarios por el valor de una clave:")
print(people)
sorted_people = sorted(people, key=lambda x: x["age"])
print(sorted_people)

# Filtrar palabras que empiezan con una vocal
print("\n")
print("Filtrar palabras que empiezan con una vocal:")
words = ['manzana', 'arandano', 'rambután', 'cereza', 'olivo', 'sandía']
word = list(filter(lambda x: x[0] in ('a','e','i','o','u'), words))
print(words)
print(word)

# Obtener la primera letra de cada palabra en una lista
print("\n")
print("Primera letra de cada palabra en una lista:")
print(words)
first_letter = list(map(lambda x: x[0], words))
print(first_letter)