# MÓDULO: Programación Orientada a Objetos en Python
# CLASE: Herencia en POO con Python
# https://platzi.com/home/clases/10002-python/70194-herencia/

# 4. Polimorfismo
# El polimorfismo permite usar una interfaz común para diferentes tipos de objetos. 
# En otras palabras, puedes llamar al mismo método en diferentes objetos y obtener comportamientos diferentes.

class Pato:
    def hacer_sonido(self):
        return "Cuac"

class Perro:
    def hacer_sonido(self):
        return "Guau"

# Función que utiliza polimorfismo
def sonido_animal(animal):
    print(animal.hacer_sonido())

# Uso
mi_pato = Pato()
mi_perro = Perro()

sonido_animal(mi_pato)  # Salida: Cuac
sonido_animal(mi_perro) # Salida: Guau

# Explicación:
# La función sonido_animal() acepta cualquier objeto que tenga un método hacer_sonido().
# Tanto Pato como Perro tienen el método hacer_sonido(), pero cada uno devuelve un sonido diferente.
# Esto permite que sonido_animal() funcione de manera flexible con distintos tipos de objetos.
