# Caso Práctico: Sistema de Gestión de Vehículos para una Empresa de Alquiler
# Supongamos que estamos desarrollando un sistema para la gestión de vehículos en una empresa de alquiler de coches. Queremos manejar diferentes tipos de vehículos (coches, motocicletas y camiones), y cada tipo de vehículo tiene características y comportamientos específicos.

# ################ 
# 1. Abstracción
# Vamos a definir una clase abstracta Vehiculo que será la base para todos los tipos de vehículos. En esta clase, definimos métodos generales como arrancar(), detener(), y mostrar_info(), sin preocuparnos por cómo se implementan en los diferentes tipos de vehículos.
from abc import ABC, abstractmethod

class Vehiculo(ABC):
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año

    @abstractmethod
    def arrancar(self):
        pass

    @abstractmethod
    def detener(self):
        pass

    @abstractmethod
    def mostrar_info(self):
        pass
# Explicación
# - Vehiculo es una clase abstracta que sirve como plantilla para todos los vehículos.
# - Utilizamos el método @abstractmethod para asegurarnos de que las clases derivadas implementen estos métodos.

# ################ 
# 2. Encapsulación
# Vamos a encapsular la lógica interna de cada vehículo, como el estado de si está en marcha o no. Esto lo haremos mediante atributos privados y métodos para interactuar con ellos.
class Coche(Vehiculo):
    def __init__(self, marca, modelo, año, num_puertas):
        super().__init__(marca, modelo, año)
        self.__num_puertas = num_puertas  # Atributo privado
        self.__en_marcha = False          # Atributo privado

    def arrancar(self):
        if not self.__en_marcha:
            self.__en_marcha = True
            print(f"{self.marca} {self.modelo} ha arrancado.")
        else:
            print(f"{self.marca} {self.modelo} ya está en marcha.")

    def detener(self):
        if self.__en_marcha:
            self.__en_marcha = False
            print(f"{self.marca} {self.modelo} se ha detenido.")
        else:
            print(f"{self.marca} {self.modelo} ya estaba detenido.")

    def mostrar_info(self):
        return f"Coche: {self.marca} {self.modelo} ({self.año}), {self.__num_puertas} puertas"
# Explicación
# - Los atributos __num_puertas y __en_marcha son privados (usando __), por lo que solo se pueden modificar a través de métodos públicos como arrancar() y detener().
# - Así, encapsulamos la lógica interna del coche para protegerla del acceso directo.


# ################ 
# 3. Herencia
# Vamos a crear diferentes tipos de vehículos (coches, motocicletas y camiones) que heredan de la clase base Vehiculo.
class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, año, tipo):
        super().__init__(marca, modelo, año)
        self.tipo = tipo  # Por ejemplo, "Deportiva" o "Cruiser"
    
    def arrancar(self):
        print(f"{self.marca} {self.modelo} motocicleta ha arrancado.")
    
    def detener(self):
        print(f"{self.marca} {self.modelo} motocicleta se ha detenido.")
    
    def mostrar_info(self):
        return f"Motocicleta: {self.marca} {self.modelo} ({self.año}), tipo {self.tipo}"

class Camion(Vehiculo):
    def __init__(self, marca, modelo, año, capacidad_carga):
        super().__init__(marca, modelo, año)
        self.capacidad_carga = capacidad_carga  # Capacidad en toneladas

    def arrancar(self):
        print(f"{self.marca} {self.modelo} camión ha arrancado.")
    
    def detener(self):
        print(f"{self.marca} {self.modelo} camión se ha detenido.")

    def mostrar_info(self):
        return f"Camión: {self.marca} {self.modelo} ({self.año}), capacidad de carga: {self.capacidad_carga} toneladas"
# Explicación:
# - Las clases Motocicleta y Camion heredan de Vehiculo.
# - Cada clase tiene su propia implementación de los métodos heredados, permitiendo especializar el comportamiento para cada tipo de vehículo.

# ################ 
# 4. Polimorfismo
# Ahora, podemos usar polimorfismo para tratar todos los vehículos de manera uniforme, independientemente de su tipo. Podemos usar una misma función para operar con distintos objetos que comparten la misma interfaz.
def mostrar_detalles(vehiculo):
    print(vehiculo.mostrar_info())
    vehiculo.arrancar()
    vehiculo.detener()
    print()  # Línea en blanco para separación

# Creamos una lista de diferentes vehículos
vehiculos = [
    Coche("Toyota", "Corolla", 2020, 4),
    Motocicleta("Yamaha", "MT-07", 2022, "Deportiva"),
    Camion("Volvo", "FH16", 2019, 20)
]

# Usamos polimorfismo para interactuar con cada tipo de vehículo
for vehiculo in vehiculos:
    mostrar_detalles(vehiculo)

# Explicación:
# - Gracias al polimorfismo, podemos usar la función mostrar_detalles() para interactuar con distintos tipos de vehículos sin necesidad de preocuparnos por su clase específica.
# - Cada objeto responde de manera diferente al método arrancar(), detener() y mostrar_info() según su propia implementación.

# Resumen de los 4 Pilares Aplicados
# 1. Abstracción: Creamos una clase Vehiculo con métodos abstractos para definir la interfaz que todos los vehículos deben seguir.
# 2. Encapsulación: Protegemos los datos internos (__num_puertas, __en_marcha) usando atributos privados.
# 3. Herencia: Creamos subclases (Coche, Motocicleta, Camion) que heredan de la clase Vehiculo, reutilizando y extendiendo su funcionalidad.
# 4. Polimorfismo: Usamos una función común para operar con diferentes tipos de vehículos, permitiendo que cada clase implemente su propio comportamiento.