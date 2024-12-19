# Módulo: Métodos y estructura de clases en Python:
# Clase: Métodos mágicos avanzados

"""
Lista completa de métodos mágicos útiles
Inicialización y finalización:

__init__: Inicializa el objeto.
__del__: Se llama cuando el objeto es eliminado.
Representación y conversión:

__str__, __repr__, __format__
Aritmética y operadores:

__add__, __sub__, __mul__, __truediv__, __floordiv__, __mod__, __pow__
Comparación:

__eq__, __ne__, __lt__, __le__, __gt__, __ge__
Acceso a contenedores:

__getitem__, __setitem__, __delitem__
__len__, __contains__
Gestión de contexto:

__enter__, __exit__
"""

print("Métodos de contexto:")
class GestorRecursos:
    """
    Métodos de contexto (__enter__ y __exit__)
    Se usan para manejar contextos con la instrucción with.
    """
    def __enter__(self):
        print("Entrando en el contexto")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Saliendo del contexto")

with GestorRecursos():
    print("Dentro del contexto")


print("\nMétodos para convertir objetos")
class Contador:
    """
    Métodos para convertir objetos
    __int__(self): Devuelve un entero (int(obj)).
    __float__(self): Devuelve un flotante (float(obj)).
    __bool__(self): Devuelve un valor booleano (bool(obj)).
    """
    def __init__(self, valor):
        self.valor = valor

    def __int__(self):
        return self.valor

    def __bool__(self):
        return self.valor > 0

contador = Contador(10)
print(int(contador))  # 10
print(bool(contador))  # True

"""
Los métodos mágicos permiten que tus clases se comporten como tipos nativos de Python, interactuando de forma natural con operadores y funciones. Si los utilizas de manera correcta, puedes crear clases muy flexibles y poderosas.
"""