# MÓDULO: Control de Flujo en Python
# CLASE: Bucles y Control de Iteraciones
# https://platzi.com/home/clases/10002-python/70091-bucles-y-control-de-iteraciones/

# Bucles y Control de Iteraciones
# Bucles en Python
# Bucle for
# Bucle for con range
# Bucle while
# Bucle for con enumerate
# Bucle for con zip
# Bucle for con iterables
# Bucle for con diccionarios
# Bucle for con sets
# Bucle for con break y continue
# Bucle for con else
# Bucle for con pass
# Bucle for con list comprehension

# Bucle for
print("Bucle for:")
numbers = [1, 2, 3, 4, 5]
for i in numbers:
    if i == 3:
        #continue omite la iteración actual y pasa a la siguiente
        continue
    print("i tiene el valor de:", i)

print("Bucle for con range:")
#for i in range(3, 15):
for i in range(5):
    print("i tiene el valor de:", i)

fruits = ["manzana", "pera", "uva", "sandía", "tomate"]
for fruit in fruits:
    print("Fruta:", fruit)
    if fruit == "sandía":
        print("¡Es una sandía!")

# Bucle while
print("\n")
print("Bucle while:")
x = 0
while x < 5:
    if x == 3:
        #break termina el bucle
        break
    x += 1
    print("x tiene el valor de:", x)
    
# Bucle for con enumerate
# enumerate() devuelve un índice y el valor de un iterable
print("\n")
print("Bucle for con enumerate:")
for index, fruit in enumerate(fruits):
    print("index:", index, "Fruta:", fruit)

# Bucle for con zip
# zip() combina dos o más listas en una sola
print("\n")
print("Bucle for con zip:")
colors = ["rojo", "verde", "azul", "amarillo", "naranja"]
for fruit, color in zip(fruits, colors):
    print("Fruta:", fruit, "| Color:", color)

# Bucle for con iterables
# Iterables son objetos que se pueden recorrer
print("\n")
print("Bucle for con iterables:")
for letter in "Arriba Alianza Lima":
    print("Letra:", letter)

# Bucle for con diccionarios
# items() devuelve una lista de tuplas con clave y valor
print("\n")
print("Bucle for con diccionarios:")
person = {"name": "Juan", "age": 25, "city": "Lima"}
for key, value in person.items():
    print("Clave:", key, "| Valor:", value)

# Bucle for con sets
# Los sets no tienen índices
print("\n")
print("Bucle for con sets:")
my_set = {1, 2, 3, 4, 5}
for element in my_set:
    print("Elemento:", element)
