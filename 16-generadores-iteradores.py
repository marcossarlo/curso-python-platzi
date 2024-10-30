# MÓDULO: Control de Flujo en Python
# CLASE: Generadores e Iteradores
# https://platzi.com/home/clases/10002-python/70188-generadores-e-iteradores/

# Generadores e Iteradores
# Generadores en Python
# Iteradores en Python
# Iteradores en Python con iter()
# Iteradores en Python con next()
# Iteradores en Python con StopIteration
# Iteradores en Python con yield
# Iteradores en Python con yield from
# Iteradores en Python con iterables
# Iteradores en Python con iter() y next()



# ejemplo con iter() y next()
# Un iterador se suele definir mediante una clase que implementa los métodos __iter__() y __next__().
print("Iteradores en Python con iter() y next():")
numbers = [1, 2, 3, 4, 5]
# iter() convierte un iterable en un iterador
numbers_iter = iter(numbers)
# next() obtiene el siguiente elemento de un iterador
print(next(numbers_iter))
print(next(numbers_iter))

# Iteradores de cadena de texto
print("\n")
print("Iteradores de cadena de texto:")
text = "Hi MarcosSarlo"
text_iter = iter(text)
for char in text_iter:
    print(char)


print("\n")
limit = 10

print("Iterador para los números impares:")
odd_limit = iter(range(1, limit+1,2))
for num in odd_limit:
    print(num)

print("Iterador para los número pares")
# range(start, stop, step)
odd_limit = iter(range(2, limit+1,2))
for num in odd_limit:
    print(num)

# generador con yield
# Un generador se define mediante una función que usa yield.
print("\n")
print("Generador de números pares con yield:")
def odd_numbers(limit):
    num = 0
    while num < limit:
        num += 2
        yield num

for num in odd_numbers(limit):
    print(num)

# Fibonacci
# 0 1 1 2 3 5 8 13 21 34 55 89 144 ...
print("\n")
print("Iterador para la secuencia de Fibonacci:")
limit = 100
def fibonacci (limit):
    a, b = 0, 1
    while a <= limit:
        yield a
        a, b = b, a + b
        
for num in fibonacci(limit):
    print(num)  