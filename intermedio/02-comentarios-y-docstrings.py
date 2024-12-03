"""
Clase: Comentarios y Docstrings en Python
https://platzi.com/home/clases/10002-python/71730-comentarios-y-docstrings-en-python/

Los comentarios y docstrings son herramientas esenciales para documentar tu código, hacerlo más legible, y facilitar su mantenimiento. Aunque no afectan la ejecución del programa, son fundamentales para que otros (o tú mismo en el futuro) entiendan el propósito del código.

"""

"""
1. Comentarios:
Los comentarios son líneas de texto que Python ignora al ejecutar el programa. Se utilizan para explicar partes del código, resaltar decisiones de diseño, o dejar notas para futuros desarrolladores.

Buenas Prácticas con Comentarios
- Se claro y conciso: Los comentarios deben explicar POR QUÉ se hace algo, no CÓMO.
- Evita comentarios redundantes: No expliques lo obvio.

"""
# No recomendado: Comentario redundante
x = 5  # Asigna 5 a x

# Recomendado: Explica el propósito
x = 5  # Valor inicial para el conteo de usuarios

"""
2. Docstrings
Los docstrings son cadenas de texto utilizadas para documentar funciones, clases y módulos. 
A diferencia de los comentarios, los docstrings están disponibles durante la ejecución del programa y pueden ser accedidos mediante la función help() o el atributo __doc__.

"""
# a) Docstrings en Funciones
def suma(a, b):
    """
    Suma dos números y devuelve el resultado.
    
    Parámetros:
    a (int o float): El primer número.
    b (int o float): El segundo número.
    
    Devuelve:
    int o float: La suma de los dos números.
    """
    return a + b

print(help(suma))  # Muestra el docstring

# b) Docstrings en Clases
class Coche:
    """
    Clase que representa un coche.
    
    Atributos:
    marca (str): La marca del coche.
    modelo (str): El modelo del coche.
    """
    
    def __init__(self, marca, modelo):
        """Inicializa los atributos marca y modelo."""
        self.marca = marca
        self.modelo = modelo

print(help(Coche))

# c) Docstrings en Módulos

"""
Este módulo realiza operaciones matemáticas básicas.
Contiene funciones para sumar, restar, multiplicar y dividir.
"""

def suma(a, b):
    """Devuelve la suma de dos números."""
    return a + b


# Buenas Prácticas para Docstrings
"""
1. Sé descriptivo: Explica el propósito, parámetros y valor de retorno.
2. Usa un estilo coherente: Puedes seguir el formato PEP 257 o Google Style.
3. Mantén los docstrings actualizados: Modifícalos si cambia el comportamiento de la función.
"""

def calcular_area(base, altura):
    """
    Calcula el área de un triángulo.
    
    Args:
        base (float): La base del triángulo.
        altura (float): La altura del triángulo.

    Returns:
        float: El área calculada del triángulo.
    """
    return (base * altura) / 2

print(help(calcular_area))

'''
Comentarios vs Docstrings 
# Comentarios ( # ):
- Explicar partes del código o decisiones de diseño.
- Solo en el código fuente, no accesible en ejecución.
- Explicación breve o notas técnicas.

# Docstrings (""")
- Documentar funciones, clases, o módulos completos.
Accesible en tiempo de ejecución con help().

Los docstrings son fundamentales para que tus funciones y clases sean fácilmente entendibles por otros desarrolladores, mientras que los comentarios te ayudan a anotar decisiones o aclaraciones en partes específicas del código.
'''
