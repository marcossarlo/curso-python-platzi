# MÓDULO: Programación Orientada a Objetos en Python
# CLASE: Herencia en POO con Python
# https://platzi.com/home/clases/10002-python/70194-herencia/

# 1. Abstracción
# La abstracción consiste en ocultar los detalles complejos y mostrar solo la información esencial. 
# Esto te permite enfocarte en lo que hace un objeto en lugar de cómo lo hace.

from abc import ABC, abstractmethod

# Creamos una clase abstracta llamada 'Animal'
class Animal(ABC):
    @abstractmethod
    def hacer_sonido(self):
        pass

# Clases concretas que heredan de la clase 'Animal'
class Perro(Animal):
    def hacer_sonido(self):
        return "El Perro hace Guau"

class Gato(Animal):
    def hacer_sonido(self):
        return "El Gato hace Miau"

# Uso
mi_perro = Perro()
mi_gato = Gato()
print(mi_perro.hacer_sonido())  # Salida: Guau
print(mi_gato.hacer_sonido())   # Salida: Miau
# Creamos una clase abstracta Animal con un método abstracto hacer_sonido().
# Las clases Perro y Gato implementan ese método, ocultando los detalles internos.
# Los detalles de cómo cada animal hace su sonido están ocultos en sus propias clases.
# En este caso, la clase 'Animal' es una clase abstracta que define un método abstracto llamado 'hacer_sonido'.