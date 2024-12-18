# Decoradores anidados con parámetros
# Combina ambas técnicas: decoradores anidados y con parámetros.

# Ejemplo práctico de un decorador anidado con parámetros:
def verificar_permisos(permiso):
    def decorador(func):
        def wrapper(*args, **kwargs):
            if permiso == "admin":
                print("Permiso concedido")
                return func(*args, **kwargs)
            else:
                print("Permiso denegado")
                return None
        return wrapper
    return decorador

def registrar_logs(func):
    def wrapper(*args, **kwargs):
        print(f"Registrando acción para la función: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@registrar_logs
@verificar_permisos("admin")
def eliminar_usuario(user_id):
    """
    Conclusión
    El truco para entenderlo es recordar:

    Evaluación: De abajo hacia arriba (cercano a la función primero).
    Ejecución: De afuera hacia adentro (externo primero).
    """
    print(f"Usuario {user_id} eliminado")

eliminar_usuario(41)
