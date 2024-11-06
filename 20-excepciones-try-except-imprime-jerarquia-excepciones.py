# MODÚLO: Funciones y Manejo de Excepciones en PytHON
# CLASE: Manejo de Excepciones y Uso de Pass (CLASE NUEVA)
# https://platzi.com/home/clases/10002-python/70971-manejo-de-excepciones-y-uso-de-pass/

# Imprime la jerarquía de excepciones en Python
# Este código utiliza recursión para recorrer y mostrar las subclases de excepciones, permitiéndote visualizar cómo están organizadas y relacionadas entre sí.

def print_exception_hierarchy(exception_class, indent=0):
    print(' ' * indent + exception_class.__name__)
    for subclass in exception_class.__subclasses__():
        print_exception_hierarchy(subclass, indent + 4)

# Imprimir la jerarquía comenzando desde la clase base Exception
print_exception_hierarchy(Exception)