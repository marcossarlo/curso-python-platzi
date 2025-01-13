class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner          # Público: cualquiera puede acceder al propietario
        self._account_type = "Ahorros"  # Protegido: accesible internamente y en subclases
        self.__balance = balance    # Privado: solo accesible dentro de esta clase

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"Depósito exitoso. Nuevo saldo: {self.__balance}"
        return "El monto debe ser positivo."

    def show_balance(self):
        return f"Saldo actual: {self.__balance}"

    def _change_account_type(self, new_type):
        self._account_type = new_type

    def __apply_fees(self):
        self.__balance -= 10  # Simula cobro de comisión

# Uso
account = BankAccount("María", 1000)
print(f"Dueño de la cuenta: {account.owner}")  # Público: María
print(account.show_balance())  # Saldo actual: 1000
# Acceso protegido (desaconsejado):
print(f"Tipo de Cuenta: {account._account_type}")  # Ahorros
# Acceso privado (no permitido):
# print(account.__balance)  # AttributeError
print(f"Balance: {account._BankAccount__balance}")  # 1000
