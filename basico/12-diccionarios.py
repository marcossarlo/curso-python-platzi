# Diccionarios
# https://platzi.com/home/clases/10002-python/70089-diccionarios/

# Un diccionario es una colección de elementos que se encuentran indexados, es decir, se accede a ellos a través de un índice.
# Los diccionarios se declaran con llaves {}.
# Los elementos de un diccionario tienen una clave y un valor.
# Los elementos de un diccionario no están ordenados.
# Los elementos de un diccionario no están indexados.
# Los valores de un diccionario pueden ser de cualquier tipo de dato.
# Los valores de un diccionario pueden ser duplicados, pero las claves no.
# Los diccionarios se pueden modificar.
# Los diccionarios son iterables.
# Los diccionarios son más rápidos que las listas.
# Los diccionarios son un tipo de dato mutable.
# Los diccionarios son un tipo de dato dinámico.
# Los diccionarios pueden ser anidados.
# Los diccionarios pueden ser retornados por una función.
# Los diccionarios pueden ser utilizados como argumentos de una función.
# Los diccionarios pueden ser utilizados como claves de un diccionario.
# Los diccionarios pueden ser utilizados como valores de un diccionario.
# Los diccionarios pueden ser utilizados como valores de una lista.
# Los diccionarios pueden ser utilizados como valores de una tupla.

numbers = {1: "Uno", 2: 2, 3: "Tres", 4: "Cuatro"}
print(type(numbers), numbers)
print(type(numbers[2]), numbers[2])
print(type(numbers[3]), numbers[3])

information = {
                'name': 'Marcos',
                'lastName': 'Sar Lo',
                'age': 45,
                'height': 1.69
            }
print(information)
print(information['name'])

print('\n')
print('Borrar un elemento de un diccionario')
del information['height']
print(information)

print('\n')
print('Obteniedo las claves del diccionario')
keys = information.keys()
print(type(keys), keys)

print('\n')
print('Obteniedo los valores del diccionario')
values = information.values()
print(type(values), values)

print('\n')
print('Obteniedo las claves, valores del diccionario')
pairs = information.items()
print('el resultado lo devuelve como una lista de tuplas:')
print(pairs)

# Agenda de contactos, donde cada contacto es un diccionario, utilizando un diccionario de diccionarios
# Agenda de contactos
print('\n')
contacts = {
    'Marcos': {
        'Nick': 'MarcosSarLo',
        'email': 'me@marcossarlo.ney',
        'phone': '1234567890'
    },
    'Juan': {
        'Nick': 'JuanGa',
        'email': 'men@juangamarra.com',
        'phone': '0987654321'
    }
}
print('Contactos: ', contacts)
print('Marcos:', contacts['Marcos'])

# Cuales son ejemplos del uso de Dicctionarios en la vida real:
# - Diccionario de contactos
# - Diccionario de productos en un supermercado
# - Diccionario de empleados en una empresa
# - Diccionario de estudiantes en una escuela
# - Diccionario de libros en una biblioteca
# - Diccionario de películas en una plataforma de streaming
# - Diccionario de canciones en una plataforma de música
# - Diccionario de recetas de cocina
# - Diccionario de rutas de transporte público
# - Diccionario de rutas de envíos
# - Diccionario de rutas de vuelos
# - Diccionario de rutas de trenes
# - Diccionario de rutas de barcos

# Ejemplos:
print('\n')
# Configuración de una aplicación
config = {
    "host": "localhost",
    "port": 8080,
    "debug": True
}
print("Configuración:", config)

# Configuración de una base de datos
database = {
    "host": "localhost",
    "port": 3306,
    "user": "root",
    "password": "123456"
}
print("Base de Datos:", database)

# Ejemplo de una biblioteca
library = {
    "1": {
        "title": "Python Programming",
        "author": "Marcos Sar Lo",
        "year": 2021
    },
    "2": {
        "title": "JavaScript Programming",
        "author": "Juan Perez",
        "year": 2020
    },
    "3": {
        "title": "Java Programming",
        "author": "Maria Lopez",
        "year": 2019
    }
}
print("Biblioteca:", library)
print("Libro 1:", library["1"])

# Ejemplo de una tienda
store = {
    "1": {
        "product": "Laptop",
        "price": 1000
    },
    "2": {
        "product": "Smartphone",
        "price": 500
    },
    "3": {
        "product": "Tablet",
        "price": 300
    }
}
print("Tienda:", store)

# Ejemplo de una plataforma de streaming
streaming = {
    "1": {
        "title": "The Mandalorian",
        "seasons": 2
    },
    "2": {
        "title": "The Witcher",
        "seasons": 1
    },
    "3": {
        "title": "Stranger Things",
        "seasons": 3
    }
}
print("Plataforma de Streaming:", streaming)