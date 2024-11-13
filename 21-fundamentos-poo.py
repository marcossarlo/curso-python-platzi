# MÓDULO: Programación Orientada a Objetos en Python
# CLASE: Fundamentos de Programación Orientada a Objetos en Python
# https://platzi.com/home/clases/10002-python/70192-fundamentos-de-programacion-orientada-a-objetos/

# 1. Introducción a la Programación Orientada a Objetos
# 2. Clases y Objetos en Python
# 3. Atributos y Métodos en Python
# 4. Métodos Especiales en Python
# 5. Encapsulamiento en Python
# 6. Herencia en Python
# 7. Polimorfismo en Python

# 1. Introducción a la Programación Orientada a Objetos
# La programación orientada a objetos es un paradigma de programación que nos permite modelar objetos del mundo real.
# En la programación orientada a objetos, los objetos son entidades que tienen atributos y comportamientos.
# Los atributos son las características de los objetos y los comportamientos son las acciones que los objetos pueden realizar.
# En la programación orientada a objetos, los objetos son instancias de clases. Las clases son plantillas que nos permiten crear objetos.
# En Python, las clases se definen con la palabra clave class.
# Los objetos se crean a partir de una clase utilizando la siguiente sintaxis: objeto = Clase().
# Los atributos de un objeto se acceden con la siguiente sintaxis: objeto.atributo.
# Los métodos de un objeto se acceden con la siguiente sintaxis: objeto.metodo().
# Los métodos son funciones que pertenecen a una clase y que pueden acceder a los atributos de un objeto.
# En Python, los métodos se definen igual que las funciones, pero dentro de una clase.
# Los métodos pueden recibir argumentos, igual que las funciones.
# Los métodos pueden devolver valores, igual que las funciones.
# Los métodos pueden modificar los atributos de un objeto, igual que las funciones.
# Los métodos especiales son métodos que tienen un significado especial en Python.
# Los métodos especiales se definen con dos guiones bajos al principio y al final del nombre.
# El método __init__ es un método especial que se ejecuta al crear un objeto.
# El método __init__ se utiliza para inicializar los atributos de un objeto.
# El encapsulamiento es un mecanismo que nos permite proteger los atributos de un objeto.
# En Python, los atributos privados se definen con dos guiones bajos al principio del nombre.
# Los métodos de un objeto pueden acceder a los atributos privados de ese objeto.
# La herencia es un mecanismo que nos permite crear una clase a partir de otra clase.
# La clase que hereda se llama subclase y la clase de la que hereda se llama superclase.
# La subclase hereda los atributos y métodos de la superclase.
# La subclase puede sobrescribir los métodos de la superclase.

class Person:
    # El método __init__ es un método especial que se ejecuta al crear un objeto.
    # El método __init__ se utiliza para inicializar los atributos de un objeto.
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # Los métodos pueden devolver valores, igual que las funciones.
    # Los métodos pueden modificar los atributos de un objeto, igual que las funciones.
    def greet(self):
        print(f"Hola, mi nombre es {self.name} y tengo {self.age} años")

print("Definiendo Clase Person:")
person1 = Person("Juan", 25)
person1.greet()

person2 = Person("María", 30)
person2.greet()

print("\nDefiniendo Clase BankAccount:")
class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
        self.is_active = True
    
    def deposit(self, amount):
        if self.is_active:
            self.balance += amount
            print(f"{self.account_holder}: Depósito realizado con {amount}. Nuevo saldo: {self.balance}")
        else:
            print("La cuenta está inactiva")
    
    def withdraw(self, amount):
        if self.is_active:
            if amount <= self.balance:
                self.balance -= amount
                print(f"{self.account_holder}: Retiro realizado con {amount}. Nuevo saldo: {self.balance}") 
            else:
                print(f"Saldo insuficiente, cantidad: {amount} | saldo: {self.balance}")
        else:
            print("La cuenta está inactiva")

    def deactivate(self):
        self.is_active = False
        print(f"{self.account_holder}: Cuenta desactivada")
    
    def activate(self):
        self.is_active = True
        print(f"{self.account_holder}: Cuenta activada")

# crear objeto BankAccount
account1 = BankAccount("Giraut", 1000)
account1.deposit(357)
account1.withdraw(2000)
account1.deactivate()
account1.activate()