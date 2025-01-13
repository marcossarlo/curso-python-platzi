class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner          # Público
        self._interest_rate = 0.05  # Protegido
        self.__balance = balance    # Privado

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"Depósito exitoso. Nuevo saldo: {self.__balance}"
        return "El monto debe ser positivo."

    def _apply_interest(self):
        self.__balance += self.__balance * self._interest_rate

    def __calculate_fees(self):
        return self.__balance * 0.02

    def show_balance(self):
        fees = self.__calculate_fees()
        return f"Saldo: {self.__balance - fees}"

# Uso
account = BankAccount("Juan", 1000)
print(account.deposit(500))  # Depósito exitoso. Nuevo saldo: 1500
print(account.show_balance())  # Saldo: 1470.0

# Acceso a protegido (desaconsejado):
print(f"Tasa de Interés: {account._interest_rate}")  # 0.05

# Acceso a privado (no permitido directamente):
# print(account.__balance)  # AttributeError
# Pero con name mangling:
print(f"Saldo de cuenta bancaria: {account._BankAccount__balance}")  # 1500
