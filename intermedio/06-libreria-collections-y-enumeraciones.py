# Librería Collections y Enumeraciones
# https://platzi.com/home/clases/10002-python/71734-libreria-collections-y-enumeraciones/

#Librería Collections:
# La librería collections de Python proporciona una colección de contenedores especializados, que son alternativas a los contenedores integrados de Python, como dict, list, set y tuple. Estos contenedores especializados son más eficientes y ofrecen funcionalidades adicionales, como valores por defecto, ordenación, conteo y más. 
# La librería collections incluye contenedores como:
# defaultdict, 
# deque, 
# Counter, 
# OrderedDict y 
# namedtuple.

# defaultdict: 
# Es una subclase de dict que permite definir un valor por defecto para las claves que no existen en el diccionario. defaultdict es útil para contar elementos, agrupar datos y realizar otras operaciones donde se necesita un valor por defecto para las claves no existentes.
from collections import defaultdict

def count_products(orders: list[str]) -> defaultdict:
    #Crea un diccionario con valor por defecto 0 
    product_count = defaultdict(int)
    print(product_count)
    for product in orders:
        # Para cada producto, incrementa el contador correspondiente en product_count
        product_count[product] +=1
    return product_count

print("Uso de defaultdict:")
orders = ['laptop', 'smartphone', 'laptop', 'tablet']
count = count_products(orders)
print(count)

# Counter:
# Counter es una subclase de dict que permite contar elementos. Counter es útil para contar elementos, agrupar datos y realizar otras operaciones donde se necesita contar elementos.
from collections import Counter

def count_products(orders: list[str]) -> Counter:
    return Counter(orders)

print("\nUso de Counter:")
#orders = ['laptop', 'smartphone', 'laptop', 'tablet']
count = count_products(orders)
print(count)

# deque:
# deque es una lista de doble extremo que permite añadir y eliminar elementos de ambos extremos de la lista de forma eficiente. 
# deque es útil para implementar colas, pilas y otras estructuras de datos donde se necesita añadir y eliminar elementos de ambos extremos de la lista.
from collections import deque

def process_orders(orders: list[str]) -> deque:
    order_queue = deque()
    for order in orders:
        order_queue.append(order)
    order_queue.append('smartwatch')
    order_queue.appendleft('smartband')
    order_queue.pop()
    order_queue.popleft()
    return order_queue

print("\nUso de deque:")
orders = ['laptop', 'smartphone', 'laptop', 'tablet']
queue = process_orders(orders)
print(queue)

# Enumeraciones:
# Las enumeraciones son una forma de crear un conjunto de constantes con nombres descriptivos.
# Las enumeraciones son útiles para definir constantes, estados, opciones y otras constantes con nombres descriptivos.
from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

def check_color(get_color: Color):
    if get_color == Color.RED:
        return "Color Rojo"
    elif get_color == Color.GREEN:
        return "Color Verde"
    elif get_color == Color.BLUE:
        return "Color Azul"
    else:
        return "Color no válido"

print("\nUso de Enumeraciones:")
print(check_color(Color.GREEN))


print(Color.RED)
print(Color.RED.name)
print(Color.RED.value)



