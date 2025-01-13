"""
@staticmethod y @classmethod

En Python, los métodos estáticos y los métodos de clase son herramientas avanzadas que permiten trabajar con clases y objetos de formas distintas a los métodos regulares. Estas dos características se implementan usando los decoradores @staticmethod y @classmethod.

"""

# 1. Métodos Estáticos (@staticmethod)
"""
¿Qué son?
Un método estático no está ligado a una instancia ni a la clase en sí. Es simplemente una función dentro de la clase que no accede ni modifica atributos de la instancia ni de la clase.
"""

from datetime import date

class Utility:
    @staticmethod
    def is_weekday():
        today = date.today()
        return today.weekday() < 5  # Devuelve True si es lunes a viernes

# Métodos Estáticos (@staticmethod)
print("Métodos Estáticos (@staticmethod):")
# Uso
print(Utility.is_weekday())  # True o False dependiendo del día

# 2. Métodos de Clase (@classmethod)
"""
Un método de clase está ligado a la clase en lugar de a una instancia. Recibe automáticamente una referencia a la clase como primer argumento, denominada convencionalmente cls.
"""

class Person:
    species = "Homo sapiens"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_birth_year(cls, name, birth_year):
        current_year = date.today().year
        age = current_year - birth_year
        return cls(name, age)

print("\nMétodos de Clase (@classmethod):")
# Uso
p = Person.from_birth_year("Juan", 1976)
print(p.name)  # Juan
print(p.age)  # Edad calculada

print("\nUso combinado:")
class Employee:
    company_name = "TechCorp"  # Atributo de clase

    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    @classmethod
    def change_company(cls, new_name):
        cls.company_name = new_name  # Modificar atributo de clase

    @staticmethod
    def calculate_bonus(salary, percentage):
        return salary * (percentage / 100)

    @classmethod
    def from_string(cls, employee_string):
        name, position, salary = employee_string.split(",")
        return cls(name, position, float(salary))

# Uso
# Crear empleados desde una cadena usando un método de clase
emp1 = Employee.from_string("Alice,Developer,70000")
print(emp1.name)  # Alice
print(emp1.salary)  # 70000.0

# Calcular bono usando un método estático
bonus = Employee.calculate_bonus(emp1.salary, 10)
print(bonus)  # 7000.0

# Cambiar el nombre de la empresa para todos los empleados
Employee.change_company("InnoTech")
print(Employee.company_name)  # InnoTech
