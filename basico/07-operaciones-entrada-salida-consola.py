# Operaciones de Entrada/Salida en Consola
# https://platzi.com/home/clases/10002-python/70085-operaciones-de-entradasalida-en-consola/

name = input("¿Cuál es tu nombre? ")
print(type(name), name)
# Si queremos que la edad sea un número entero en lugar de un string, usamos el Casting (Cambiar el tipo de dato)
age = int(input("¿Cuál es tu edad? "))
print(type(age), age)
print(f"Hola {name}, tienes {age} años")
