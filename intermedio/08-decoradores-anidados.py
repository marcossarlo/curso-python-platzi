# Decoradores anidados
# Un decorador anidado combina varios niveles de lógica dentro de un decorador. Es útil para funciones complejas donde varias operaciones deben realizarse en secuencia.
# Conclusión
# El truco para entenderlo es recordar:
# Evaluación: De abajo hacia arriba (cercano a la función primero).
# Ejecución: De afuera hacia adentro (externo primero).

print("\nDecoradores anidados:")
def decorador_1(func):
    def wrapper_1(*args, **kwargs):
        print("Antes de decorador 1")
        resultado = func(*args, **kwargs)
        print("Después de decorador 1")
        return resultado
    return wrapper_1

def decorador_2(func):
    def wrapper_2(*args, **kwargs):
        print("Antes de decorador 2")
        resultado = func(*args, **kwargs)
        print("Después de decorador 2")
        return resultado
    return wrapper_2

@decorador_1
@decorador_2
def mostrar_mensaje():
    print("Hola desde la función principal")

mostrar_mensaje()

