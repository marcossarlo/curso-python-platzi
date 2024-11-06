# MODÚLO: Funciones y Manejo de Excepciones en PytHON
# CLASE: ¿Cómo realizar una función recursiva en Python?
# https://platzi.com/home/clases/10002-python/70191-recursividad/

# Ejemplo: Sumatoria de los números naturales
# El caso base es la sumatoria de 0 =  0.
# El caso recursivo es la sumatoria de un número n, que es n + sumatoria(n-1).
def summation(n):
    if n < 0:
        return "No existe la sumatoria de un número negativo"
    elif n == 0:
        return 0
    else:
        print(n)
        return n + summation(n - 1)
    
try:
    number = int(input("Ingresa un número: "))
    print(f"Sumatoria de los números naturales hasta {number} es: {summation(number)}")
except ValueError:
    print("Por favor, ingresa un número entero válido.")
