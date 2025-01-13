"""
La gestión avanzada de propiedades en Python se realiza mediante el uso del decorador @property, que permite definir métodos en una clase que actúan como si fueran atributos, proporcionando una forma elegante y controlada de manejar el acceso, modificación y eliminación de atributos.

Este mecanismo es especialmente útil cuando deseas realizar validaciones, cálculos o efectos colaterales al interactuar con los atributos de una clase sin cambiar la interfaz pública.

Ventajas del Uso de Propiedades
Encapsulación: Permite encapsular la lógica de acceso a atributos sin cambiar la interfaz pública de la clase.
Validación: Puedes añadir validaciones al leer o escribir valores.
Compatibilidad: Puedes convertir atributos en propiedades sin cambiar el código que utiliza tu clase.
Flexibilidad: Facilita la adición de lógica adicional al acceso o modificación de atributos.
"""

# Ejemplo: Gestión de una cuenta bancaria
# Este ejemplo combina validación, cálculo dinámico y encapsulación:

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, amount):
        if amount < 0:
            raise ValueError("El saldo no puede ser negativo.")
        self._balance = amount

    @property
    def is_overdrawn(self):
        return self._balance < 0

# Uso
account = BankAccount("María", 1000)
print(account.balance)  # 1000

account.balance = 2000  # Actualización válida
print(account.balance)  # 2000

# Validación
# account.balance = -500  # ValueError: El saldo no puede ser negativo.

print(account.is_overdrawn)  # False
