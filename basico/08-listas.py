# Listas:
# Son colecciones de elementos que pueden ser de diferentes tipos.
# Nos facilita la tarea de permitir la manipulación y almacenamiento de datos diversos de manera estructurada y eficiente.
# https://platzi.com/home/clases/10002-python/70086-listas/

toDo = [
        "Tarea 1",
        "Tarea 2",
        "Tarea 3", 
        "Tarea 4",
        "Tarea 5"
        ]
print(type(toDo), toDo)

numbers = [1, 2, 3, "cuatro", 5]
print(type(numbers), numbers)

# Las listas en Python pueden almacenar múltiples tipos de datos, incluyendo cadenas, números enteros, números flotantes y valores booleanos. También pueden contener otras listas
print("\n")
mixedList = [toDo, True, ["Ene", "Feb", "Mar"]]
print(mixedList)
print("1er. elemento: ", mixedList[0])
print("2do. elemento: ", mixedList[1])
print("Último elemento: ", mixedList[-1])
print("Longitud de la lista:", len(mixedList))

print("\n")
print("Slicing:")
print("start: El índice donde comienza el slicing (incluido).")
print("stop: El índice donde termina el slicing (excluido).")
print("step: El tamaño del paso del slicing.")
mixedList1 = ["Uno", 2, 3, 4, True, ["Ene", "Feb", "Mar"]]
print("mixedList1: ", mixedList1)
print(mixedList1[2:4])
print(mixedList1[:2])
print(mixedList1[2:])

print("\n")
print("Añadir elementos al final con append()")
mixedList1.append("Cinco")
print(mixedList1)
mixedList1.append(["Jun", "Jul", "Ago"])
print(mixedList1)

print("\n")
print("Insertar elementos en una posición específica: insert()")
print(mixedList1)
mixedList1.insert(0, 11)
print(mixedList1)
mixedList1.insert(3, "Dos")
print(mixedList1)

print("\n")
print("Encontrar la posición de la primera aparición de un elemento con index()")
print(mixedList1)
print(mixedList1.index(['Ene', 'Feb', 'Mar']))

print("\n")
print("Encontrar el mayor y menor elemento: max() y min()")
numbers = [1, 2, 33, 41, 58.7]
print(numbers)
print("Mayor: ", max(numbers))
print("Menor: ", min(numbers))

print("\n")
print("Eliminar elementos de una lista")
print(numbers)

del numbers[-1]
print(numbers)

del numbers[:2]
print(numbers)

del numbers
print(numbers)

# print("\n")
# print("Operaciones con Listas:")
# print(mixedList1)
# print("Longitud de la lista: ", len(mixedList1))
# print("Concatenación de listas: ", mixedList + mixedList1)
# print("Repetición de listas: ", mixedList1 * 3)
# print("Búsqueda de elementos: ", "Uno" in mixedList1)



