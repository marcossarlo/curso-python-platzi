class Vehiculo:
    def __init__(self, modelo, marca, precio):
        self.modelo = modelo
        self.marca = marca
        self.precio = precio
        self.disponible = True

    def vender(self):
        if self.disponible:
            self.disponible = False
            print(f"{self.modelo} ha sido vendido.")
        else:
            print(f"{self.modelo} no está disponible.")

class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.vehiculos_comprados = []

    def comprar_vehiculo(self, vehiculo):
        if vehiculo.disponible:
            vehiculo.vender()
            self.vehiculos_comprados.append(vehiculo)
        else:
            print(f"{vehiculo.modelo} no se puede comprar.")
    
    def vender_vehiculo(self, vehiculo):
        if vehiculo in self.vehiculos_comprados:
            vehiculo.comprar()
            self.vehiculos_comprados.remove(vehiculo)
        else:
            print(f"{vehiculo.modelo} no está en la lista de vehículos comprados.")

class Concesionaria:
    def __init__(self):
        self.vehiculos = []
    
    def agregar_vehiculo(self, vehiculo):
        self.vehiculos.append(vehiculo)
        print(f"{vehiculo.modelo} ha sido agregado a la concesionaria.")
    
    def quitar_vehiculo(self, vehiculo):
        self.vehiculos.remove(vehiculo)
        print(f"{vehiculo.modelo} ha sido vendido de la concesionaria.")
    
    def mostrar_vehiculos_disponibles(self):
        for vehiculo in self.vehiculos:
            if vehiculo.disponible:
                print(f"- {vehiculo.modelo} - {vehiculo.precio}")

concesionaria = Concesionaria()
auto1 = Vehiculo("Modelo S", "Tesla", 75000)
auto2 = Vehiculo("Civic", "Honda", 20000)

concesionaria.agregar_vehiculo(auto1)
concesionaria.agregar_vehiculo(auto2)
concesionaria.mostrar_vehiculos_disponibles()

usuario = Usuario("Carlos")
usuario.comprar_vehiculo(auto1)
concesionaria.mostrar_vehiculos_disponibles()