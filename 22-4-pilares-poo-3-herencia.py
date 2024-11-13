# MÓDULO: Programación Orientada a Objetos en Python
# CLASE: Herencia en POO con Python
# https://platzi.com/home/clases/10002-python/70194-herencia/

# 3. Herencia
# La herencia permite crear una nueva clase a partir de una clase existente. 
# La clase nueva (subclase) hereda atributos y métodos de la clase existente (superclase), lo que promueve la reutilización del código.

# Clase base (superclase)
class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def mostrar_info(self):
        return f"Vehículo: {self.marca} {self.modelo}"

# Clase derivada (subclase)
class Coche(Vehiculo):
    def __init__(self, marca, modelo, puertas):
        super().__init__(marca, modelo)
        self.puertas = puertas

    def mostrar_info(self):
        return f"Coche: {self.marca} {self.modelo}, {self.puertas} puertas"

# Uso
auto = Vehiculo("Monark", "Bike Xz54")
print(auto.mostrar_info())  # Salida: Vehículo: Toyota Corolla

mi_coche = Coche("Toyota", "Corolla", 4)
print(mi_coche.mostrar_info())  # Salida: Coche: Toyota Corolla, 4 puertas
# Explicación:
# - La clase Coche hereda de la clase Vehiculo.
# - Gracias a la herencia, Coche puede usar el método mostrar_info() de Vehiculo, pero también puede sobrescribirlo (como hicimos aquí).
# - En este caso, la clase Coche sobrescribe el método mostrar_info() para mostrar información adicional (número de puertas).
# - Esto facilita la reutilización y extensión del código.

