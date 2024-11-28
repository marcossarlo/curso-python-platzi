# Clase: Librerías: Os, Math y Random
# https://platzi.com/home/clases/10002-python/70976-libreria-os-math-y-random/

# os permite interactuar con el sistema operativo. Proporciona funciones para manejar archivos, directorios, procesos, y variables de entorno.
import os
print("\nUso de la libreria OS")

# Obtener el directorio de trabajo actual
cwd = os.getcwdb()
print(f"El directorio de trabajo actual: {cwd}")

# LIstar los archivos y directorios en el directorio actual
files = os.listdir()
#print(f"Archivos y directorios en el directorio actual: {files}")

# Listar los archivos .txt en el directorio actual
txt_files = [file for file in files if file.endswith('.txt')]
print(f"Archivos .txt en el directorio actual: {txt_files}")

"""
os.mkdir('nueva_carpeta')
os.rmdir('nueva_carpeta')
"""

# math proporciona funciones y constantes matemáticas avanzadas, como trigonometría, logaritmos, y redondeos.
# Libreria MATH 
import math
print("\nUso de la libreria MATH")

# Hallar el area y perimeter de un círculo
radius = 5
area = math.pi * radius ** 2
perimeter = 2 * math.pi * radius
print(f"Area del círculo: {area}")
print(f"Perímetro del círculo: {perimeter}")

# Area del cirulo
# A = πr^2
def area_circulo(radio):
    return math.pi * math.pow(radio, 2)

print(f"Área del círculo: {area_circulo(5)}")


# Librería RANDOM
# La librería random en Python proporciona funciones para generar números aleatorios.
import random
print("\nUso de la libreria RANDOM")

# Generar un número entero aleatorio
random_int = random.randint(1, 10)
print(f"Número entero aleatorio: {random_int}")

# Elegir colores aleatorios
colors = ['rojo', 'azul', 'verde', 'amarillo', 'naranja']
random_color = random.choice(colors)
print(f"Color aleatorio: {random_color}")

# Barajar una lista de cartaas
cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
random.shuffle(cards)
print(f"Barajar una lista de cartas: {cards}")

# Estas librerías forman parte de la biblioteca estándar de Python, lo que significa que están listas para usarse sin necesidad de instalación. Su combinación permite trabajar de manera eficiente en una gran variedad de proyectos.

