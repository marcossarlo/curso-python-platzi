# MÓDULO: Programación Orientada a Objetos en Python
# CLASE: Herencia en POO con Python
# https://platzi.com/home/clases/10002-python/70194-herencia/

# 2. Encaupsulación
# La encapsulación consiste en agrupar datos y métodos que operan sobre esos datos dentro de una misma clase. 
# Además, permite restringir el acceso a ciertos atributos y métodos usando modificadores de acceso (private, protected).

# como se define un modificador de acceso private?
# se define con dos guiones bajos antes del nombre del atributo
# por ejemplo: __saldo
# ¿Cómo se accede a un atributo privado?
# Se puede acceder a un atributo privado mediante un método público que lo devuelva o lo modifique.

# como se define un modificador de acceso protected?
# se define con un guion bajo antes del nombre del atributo
# por ejemplo: _saldo
# ¿Cómo se accede a un atributo protected?
# Se puede acceder a un atributo protected desde la misma clase y desde las subclases.

class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo  # Atributo privado (2_)

    def depositar(self, cantidad):
        print(f"Deposito de {cantidad} realizado")
        self.__saldo += cantidad

    def retirar(self, cantidad):
        if cantidad <= self.__saldo:
            self.__saldo -= cantidad
            print(f"Retiro de {cantidad} realizado")
        else:
            print("Fondos insuficientes")

    def mostrar_saldo(self):
        print(f"Tu saldo es de: {self.__saldo}")

# Explicación:
# - El atributo __saldo es privado y solo puede ser accedido desde la misma clase.
# - Los métodos depositar() y retirar() permiten modificar el saldo.
# - El método mostrar_saldo() permite mostrar el saldo actual.


# Uso
cuenta = CuentaBancaria("Marcos", 1000)
cuenta.mostrar_saldo()

cuenta.depositar(500)
cuenta.mostrar_saldo()

cuenta.retirar(2200)         
cuenta.mostrar_saldo()
