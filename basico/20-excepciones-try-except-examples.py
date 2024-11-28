# MODÚLO: Funciones y Manejo de Excepciones en PytHON
# CLASE: Manejo de Excepciones y Uso de Pass (CLASE NUEVA)
# https://platzi.com/home/clases/10002-python/70971-manejo-de-excepciones-y-uso-de-pass/

# Manejo de errores al convertir a entero
print("Manejo de errores al convertir a entero")
def convertir_a_entero(valor):
    try:
        return int(valor)
    except ValueError:
        return "Error: No se puede convertir a un número entero"
num = input("Ingresa un número: ")
print(convertir_a_entero(num))

# Manejo de archivos inexistentes
print("\nManejo de archivos inexistentes")
def leer_archivo(ruta):
    try:
        with open(ruta, 'r') as archivo:
            contenido = archivo.read()
            return contenido
    except FileNotFoundError:
        return "Error: El archivo no existe"

print(leer_archivo("01-hello.py"))  # Supone que el archivo existe
print(leer_archivo("no_existe.txt"))  # Error: El archivo no existe


# Acceso a índices fuera de rango en una lista
print("\nAcceso a índices fuera de rango en una lista")
def obtener_elemento(lista, indice):
    try:
        return lista[indice]
    except IndexError:
        return "Error: Índice fuera de rango"

mi_lista = [1, 2, 3, 4, 5]
print(obtener_elemento(mi_lista, 2))  # Salida: 3
print(obtener_elemento(mi_lista, 10))  # Salida: Error: Índice fuera de rango

# El bloque else se ejecuta si no se produce ninguna excepción en el bloque try
def dividir(a, b):
    try:
        resultado = a / b
    except ZeroDivisionError:
        return "Error: División por cero no permitida"
    else:
        return f"El resultado es {resultado}"

print(dividir(10, 2))  # Salida: El resultado es 5.0
print(dividir(10, 0))  # Salida: Error: División por cero no permitida

    