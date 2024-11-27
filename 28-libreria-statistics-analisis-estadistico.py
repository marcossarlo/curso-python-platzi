# Clase: Librería Statistics y Análisis Estadístico
# https://platzi.com/home/clases/10002-python/70977-libreria-statistics-y-analisis-estadistico/

# La librería statistics en Python es un módulo estándar que proporciona funciones para realizar análisis estadístico básico. Esta librería es ideal para tareas como calcular la media, mediana, moda, desviación estándar, entre otras. Es una excelente opción cuando necesitas realizar análisis estadísticos simples sin la complejidad de bibliotecas más avanzadas como NumPy o pandas.

# ¿Por Qué Usar statistics?
# Fácil de usar: No necesitas instalar librerías externas, ya que es parte de la biblioteca estándar de Python.
# Ideal para análisis simples: Si solo necesitas hacer cálculos estadísticos básicos, es una solución rápida y eficiente.
# Funciones intuitivas: Proporciona funciones con nombres que son fáciles de entender y utilizar.

# Resumen
# La librería statistics es ideal para análisis estadísticos simples y rápidos.
# Proporciona funciones para media, mediana, moda, desviación estándar, y más.
# Útil para principiantes o para situaciones en las que no necesitas análisis complejo.

import statistics
import csv

# Leer los datos de ventas mensuales de un archivo CSV
# y calcular la media, mediana, moda, varianza y desviación estándar

file_path = '28-mounthly-sales.csv'
monthly_sales = {} # Diccionario para almacenar las ventas mensuales

with open(file_path, 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        month = row['month']
        sales = int(row['sales'])
        monthly_sales[month] = sales

sales = list(monthly_sales.values()) # Lista de ventas mensuales, solo el valor

# Calcular la media:
# se calcula sumando todos los valores de un conjunto de datos y dividiendo entre la cantidad de valores.
mean = statistics.mean(sales)
print(f'Media de las ventas: {mean}')

# Calcular la mediana:
# es el valor que separa la mitad superior de la mitad inferior de un conjunto de datos ordenado.
median = statistics.median(sales)
print(f'Mediana de las ventas: {median}')

# Calcular la moda:
# es el valor que aparece con mayor frecuencia en un conjunto de datos
mode = statistics.mode(sales)
print(f'Moda de las ventas: {mode}')

# Calcular Multimoda:
# Si hay un empate en la frecuencia de varios elementos, puedes usar statistics.multimode() para obtener una lista de las modas.
multi_mode = statistics.multimode(sales)
print(f'Multimo de las ventas: {multi_mode}')

# Calcular la varianza:
# es el promedio de los cuadrados de las diferencias entre cada valor y la media del conjunto de datos
variance = statistics.variance(sales)
print(f'Varianza de las ventas: {variance}')

# Calcular la desviación estándar:
# mide la dispersión de los datos en relación con la media
stdev = statistics.stdev(sales)
print(f'Desviación estándar de las ventas: {stdev}')

max_sales = max(sales)
min_sales = min(sales)

range_sales = max_sales - min_sales
print(f"Rango de ventas: {range_sales}")


