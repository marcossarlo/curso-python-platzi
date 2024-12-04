# Clase: Anotaciones
# https://platzi.com/home/clases/10002-python/71732-anotaciones-de-tipo/

# Anotaciones:

#IDs empleados
id1: int = 100
id2: int = 101

# Sumar los Ids
total_id: int = id1 + id2
print(total_id)

# Utilizando Funciones
def sum_ids(id1: int, id2: int) -> int:
    return id1 + id2
print("\fUtilizando Funciones")
print(sum_ids(100, 201))

 # Utilizando Clases:
class Employee:
    name: str
    age: int
    salary: float

    def __init__(self, name: str, age: int, salary: float):
        self.name = name
        self.age = age
        self.salary = salary

    def introduce(self) -> str:
        return f"Me llamo {self.name}, tengo {self.age} años y gano {self.salary} dólares."

print("\fUtilizando Clases")
employee1 = Employee("Juan", 45, 9500)
print(employee1.introduce())