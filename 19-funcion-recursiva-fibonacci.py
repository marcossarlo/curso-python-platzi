# MODÚLO: Funciones y Manejo de Excepciones en PytHON
# CLASE: ¿Cómo realizar una función recursiva en Python?
# https://platzi.com/home/clases/10002-python/70191-recursividad/

# Fibonacci
# La sucesión de Fibonacci es una serie de números en la que cada número es la suma de los dos números anteriores.
# La sucesión de Fibonacci comienza con 0 y 1.
# Los primeros números de la sucesión de Fibonacci son: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
# La sucesión de Fibonacci se puede definir de forma recursiva como:
# fibonacci(n) = fibonacci(n-1) + fibonacci(n-2)
# El caso base de la sucesión de Fibonacci es:
# fibonacci(0) = 0
# fibonacci(1) = 1
# fibonacci(2) = 1
# fibonacci(3) = 2
# fibonacci(4) = 3
# fibonacci(5) = 5
# fibonacci(6) = 8
# fibonacci(7) = 13
# fibonacci(8) = 21
# fibonacci(9) = 34
# fibonacci(10) = 55

# Ejemplo: Fibonacci de un número

def fibonacci(n):
    if n < 0:
        return "No existe el fibonacci de un número negativo"
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

number = 10
print(f"Fibonacci de {number} es {fibonacci(number)}")

