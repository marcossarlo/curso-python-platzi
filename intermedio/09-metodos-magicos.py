# Módulo: Métodos y estructura de clases en Python:
# Clase: Métodos mágicos
#https://platzi.com/home/clases/10002-python/71738-metodos-magicos/

# Los métodos mágicos en Python (también conocidos como special methods o dunder methods, porque comienzan y terminan con __) son funciones predefinidas que puedes implementar en tus clases para definir o modificar comportamientos especiales.
# Estos métodos permiten que las instancias de tus clases interactúen con operadores, funciones integradas o comportamientos específicos del lenguaje, como sumar objetos, comparar valores, convertir a cadenas, etc.

print("Métodos de inicialización y representación:\n __init__(self, ...), __str__(self):, __repr__(self)")
class Persona:
    """
    Clase Persona con métodos de inicialización y representación:
    __init__(self, ...): Se llama al crear una nueva instancia para inicializar atributos.
    __str__(self): Devuelve una representación amigable para humanos del objeto.
    __repr__(self): Devuelve una representación oficial del objeto, más útil para desarrolladores.
    """
    def __init__(self, nombre: str, edad: int):
        self.nombre = nombre
        self.edad = edad

    def __str__(self) -> str:
        return f"{self.nombre}, {self.edad} años"

    def __repr__(self) -> str:
        return f"Persona(nombre='{self.nombre}', edad={self.edad})"

persona = Persona("Marcos", 30)
print(str(persona))  # Marcos, 30 años
print(repr(persona))  # Persona(nombre='Marcos', edad=30)


print("\nMétodos de comparación:\n __eq__(self, other), __ne__(self, other), __lt__(self, other), __le__(self, other), __gt__(self, other), __ge__(self, other)")
class Producto:
    """
    Clase Producto con métodos de comparación:
    __eq__(self, other): Define el comportamiento de ==.
    __lt__(self, other): Define el comportamiento de <.
    __gt__(self, other): Define el comportamiento de >.

    """
    def __init__(self, nombre: str, precio: float) -> None:
        self.nombre = nombre
        self.precio = precio

    def __eq__(self, other) -> bool:
        return self.precio == other.precio

    def __lt__(self, other) -> bool:
        return self.precio < other.precio

producto1 = Producto("Laptop", 1000)
producto2 = Producto("Celular", 800)

print(producto1 == producto2)  # False
print(producto1 < producto2)   # False
print(producto2 < producto1)   # True


print("\nMétodos de operadoresaritmética:\n __add__(self, other), __sub__(self, other), __mul__(self, other), __truediv__(self, other), __floordiv__(self, other), __mod__(self, other), __pow__(self, other)")
class Vector:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __add__(self, other): # Define el comportamiento de +.
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(1, 2)
v2 = Vector(3, 4)
print(v1 + v2)  # Vector(4, 6)


print("\nMétodos relacionados con contenedores:\n __contains__(self, item)")  
class MiLista:
    """
    Métodos relacionados con contenedores:
    __len__(self): Se llama cuando usas len(obj).
    __getitem__(self, key): Permite acceder a elementos como si fuera una lista o diccionario.
    __setitem__(self, key, value): Permite asignar valores.
    """
    def __init__(self):
        self.datos = []

    def __len__(self):
        return len(self.datos)

    def __getitem__(self, index):
        return self.datos[index]

    def __setitem__(self, index, value):
        self.datos[index] = value

    def __str__(self):
        return str(self.datos)

lista = MiLista()
lista.datos.extend([1, 2, 3])
print(len(lista))  # 3
print(lista[1])    # 2
lista[1] = 10
print(lista)       # [1, 10, 3]

