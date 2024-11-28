# Método slice
# https://platzi.com/home/clases/10002-python/70087-metodo-slice/
# Cuando asignamos una lista a una nueva variable, por ejemplo, B = A, no estamos creando una copia independiente. Ambas variables apuntan al mismo espacio de memoria. Así, cualquier cambio en A se reflejará en B.

print('Cuando asignamos una lista a una nueva variable, por ejemplo, B = A, no estamos creando una copia independiente. Ambas variables apuntan al mismo espacio de memoria. Así, cualquier cambio en A se reflejará en B.')

numbers1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers2 = numbers1

print("numbers2 = numbers1")
print("numbers1: ", numbers1)
print("numbers2: ", numbers2)

print("\n")
print('Eliminar un valor de la lista numbers1\n esto afectará a las 2 listas:')
del numbers1[1]
print("numbers1: ", numbers1)
print("numbers2: ", numbers2)
print('Consultar el ID de ambas listas')
print("numbers1: ", id(numbers1))
print("numbers2: ", id(numbers2))

print("\n")
print('Para crear una copia independiente de una lista, usamos el método slice:')
numbers3 = numbers1[:]
# numbers3 = numbers1.copy()
print("numbers1: ", numbers1, id(numbers1))
print("numbers2: ", numbers2, id(numbers2))
print("numbers3: ", numbers3, id(numbers3))

print('Apregando un elemento a la lista numbers1, solo afectará a numbers2 y NO a numbers3')
numbers1.append(11)
print("numbers1: ", numbers1)
print("numbers2: ", numbers2)
print("numbers3: ", numbers3)