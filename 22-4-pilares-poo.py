# MÓDULO: Programación Orientada a Objetos en Python
# CLASE: Herencia en POO con Python
# https://platzi.com/home/clases/10002-python/70194-herencia/

# Los 4 pilares de la programacion orientada a objetos
# 1. Encapsulación:
#   - Permite agrupar datos y métodos en una sola unidad.
#   - Permite ocultar los detalles de implementación y exponer solo lo necesario.
#   - Permite proteger los datos y métodos de modificaciones no autorizadas.
#   - Permite restringir el acceso a los datos y métodos.
# 2. Abstracción:
#   La abstracción consiste en ocultar los detalles complejos y mostrar solo la información esencial. 
#   Esto te permite enfocarte en lo que hace un objeto en lugar de cómo lo hace.
# 3. Polimorfismo:
#   - Permite definir métodos con el mismo nombre pero con diferente implementación.
#   - Permite redefinir métodos de la clase padre en las subclases.
#   - Permite definir métodos abstractos que deben ser implementados en las subclases.
#   - Permite definir métodos que pueden recibir diferentes tipos de datos.
# 4. Herencia
#   - La herencia es una de las características más importantes de la programación orientada a objetos.
#   - Nos permite definir una clase hija que hereda todos los métodos y atributos de la clase padre.
#   - La herencia nos permite reutilizar código y también nos permite crear clases más especializadas.

# Resumen:
# - Abstracción: Ocultar detalles complejos y exponer solo lo necesario.
# - Encapsulación: Proteger los datos de acceso no autorizado y agrupar atributos y métodos en una clase.
# - Herencia: Crear nuevas clases basadas en clases existentes para reutilizar y extender el código.
# - Polimorfismo: Usar una interfaz común para objetos de diferentes tipos, permitiendo comportamientos diferentes.

class Vehicle:
    def __init__(self, brand, model, price):
        # Encapsulación
        self.brand = brand
        self.model = model
        self.price = price
        self.is_available = True

    def sell(self):
        if self.is_available:
            self.is_available = False
            print(f"El vehículo {self.brand} - {self.model} ha sido vendido.")
        else:
            print(f"El vehículo {self.model} no está disponible.")
    # Abstracción
    def check_availability(self):
        return self.is_available
    # Abstracción
    def get_price(self):
        return self.price
    
    def start_engine(self):
        raise NotImplementedError("Este método debe ser implementado en la subclase")
    
    def stop_engine(self):
        raise NotImplementedError("Este método debe ser implementado en las subclases")
# Herencia
class Car(Vehicle):
    # Polimorfismo
    def start_engine(self):
        if not self.is_available:
            return f"El motor del coche {self.brand} está en marcha"
        else:
            return f"El coche {self.brand} no está disponible"
    
    # Polimorfismo
    def stop_engine(self):
        if self.is_available:
            return f"El motor del coche {self.brand} se ha apagado"
        else:
            return f"El coche {self.brand} no está disponible"

class Bike(Vehicle):
    def start_engine(self):
        if not self.is_available:
            return f"La bicicleta {self.brand} está en marcha"
        else:
            return f"La bicicleta {self.brand} no está disponible"
    
    def stop_engine(self):
        if self.is_available:
            return f"La bicicleta {self.brand} se ha detenido"
        else:
            return f"La bicicleta {self.brand} no está disponible"

class Truck(Vehicle):
    def start_engine(self):
        if not self.is_available:
            return f"El camión del coche {self.brand} está en marcha"
        else:
            return f"El camión {self.brand} no está disponible"
    
    def stop_engine(self):
        if self.is_available:
            return f"El camión del coche {self.brand} se ha apagado"
        else:
            return f"El camión {self.brand} no está disponible"

class Customer:
    def __init__(self, name):
        self.name = name
        self.purchased_vehicles = []
    
    def buy_vehicle(self, vehicle: Vehicle):
        if vehicle.check_availability():
            vehicle.sell()
            self.purchased_vehicles.append(vehicle)
        else:
            print(f"El vehículo {vehicle.brand} - {vehicle.model} no está disponible")
    
    def inquire_vehicle(self, vehicle: Vehicle):
        if vehicle.check_availability():
            availability = "Disponible"
        else:
            availability = "No disponible"
        print(f"\nEl vehículo {vehicle.brand} - {vehicle.model} está {availability} y tiene un precio de {vehicle.get_price()}")
    
class Dealership:
    def __init__(self):
        self.inventory = []
        self.customers = []

    def add_vehicle(self, vehicle: Vehicle):
        self.available = True
        self.inventory.append(vehicle)
        print(f"{vehicle.brand} - {vehicle.model} vehículo añadido al inventario")
    
    def register_customer(self, customer: Customer):
        self.customers.append(customer)
        print(f"El cliente {customer.name} ha sido registrado")
    
    def show_available_vehicles(self):
        print("\nVehículos disponibles:")
        for vehicle in self.inventory:
            if vehicle.check_availability():
                print(f"- {vehicle.brand} - {vehicle.model} por {vehicle.get_price()}")

car1 = Car("Toyota", "Corolla", 15000)
car2 = Car("Renault", "Logan-Stepway", 25000)
car3 = Car("Ford", "Mustang", 55000)
bike1 = Bike("BMX", "X1", 500)
truck1 = Truck("Chevrolet", "NHR", 45000)

customer1 = Customer("Juan")

dealership = Dealership()
dealership.add_vehicle(car1)
dealership.add_vehicle(car2)
#dealership.add_vehicle(car3)
dealership.add_vehicle(bike1)
dealership.add_vehicle(truck1)

dealership.show_available_vehicles()

# Consultar vehículo
customer1.inquire_vehicle(car3)

# Comprar vehículo
customer1.buy_vehicle(car3)

dealership.show_available_vehicles()
customer1.inquire_vehicle(car3)


    
