# Ejercicios

# Doble de los Números
# Dada una lista de números [1, 2, 3, 4, 5], crea una nueva lista que contenga el doble de cada número usando una List Comprehension.
print("1. Doble de los Números")
numbers = [1, 2, 3, 4, 5]
print("Lista de Números:", numbers)
doubles = [number * 2 for number in numbers]
print("Doble de los Números:", doubles)

print("\n")
print("2. Filtrar y Transformar en un Solo Paso:")
# Tienes una lista de palabras ["sol", "mar", "montaña", "rio", "estrella"] y quieres obtener una nueva lista con las palabras que tengan más de 3 letras y estén en mayúsculas.
words = ["sol", "mar", "montaña", "rio", "estrella"]
print("Lista de Palabras:", words)
filtered_words = [word.upper() for word in words if len(word) > 3]
print("Palabras en Mayúsculas con más de 3 letras:", filtered_words)

# Crear un Diccionario con List Comprehension
print("\n")
print("3. Crear un Diccionario con List Comprehension")
# Tienes dos listas, una de claves ["nombre", "edad", "ocupación"] y otra de valores ["Juan", 30, "Ingeniero"]. Crea un diccionario combinando ambas listas usando una List Comprehension.
keys = ["name", "age", "occupation"]
values = ["Marcos", 45, "Ingeniero Informático"]
print("Lista de Claves:", keys)
print("Lista de Valores:", values)
dictionary = {key: value for key, value in zip(keys, values)}
print("Diccionario:", dictionary)
diccionario = {keys[i]: values[i] for i in range(len(keys))}
print("Diccionario:", diccionario)

# Extraer Información de una Lista de Diccionarios
# Dada una lista de diccionarios que representan personas:
# Extrae una lista de nombres de personas que viven en “Madrid” y tienen más de 30 años.
print("\n")
print("4. Extraer Datos de una Lista de Diccionarios")
persons = [
    {'name': 'Antuan', 'age': 25, 'city': 'Madrid'},
    {'name': 'Marcos', 'age': 45, 'city': 'Madrid'},
    {'name': 'Pedro', 'age': 35, 'city': 'Madrid'},
    {'name': 'María', 'age': 40, 'city': 'Londres'}
]
print("Lista de Personas:", persons)

# Extrae una lista de nombres de personas que viven en “Madrid” y tienen más de 30 años.
extract = [person for person in persons if person['city'] == 'Madrid' and person['age'] > 30]
print("Personas de Madrid mayores de 30 años:")
print(extract)

# List Comprehension con un else
# Dada una lista de números [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], crea una nueva lista multiplicando por 2 los números pares y dejando los impares como están.
print("\n")
print("5. List Comprehension con un else")
numbers = [x+1 for x in range(10)]
print('Lista de números:', numbers)
numbers_even = [number * 2 if number % 2 == 0 else number for number in numbers]
print('Lista de números pares * 2 :', numbers_even)
numbers_even_odd = [number * 2 if number % 2 == 0 else number * 3 for number in numbers]
print('Lista de números pares * 2 e impares * 3:', numbers_even_odd)

# Crear una Transpuesta de una Matriz
print("\n6. Crear una Transpuesta de una Matriz")
matrix = [
    [1, 2, 3], 
    [4, 5, 6], 
    [7, 8, 9]
]
print("Matriz Original:", matrix)
transpose = [[row[i] for row in matrix] for i in range(len(matrix))]

# forma extensa de hayar la transpuesta de una matriz:
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

