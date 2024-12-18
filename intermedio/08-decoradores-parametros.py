# Decoradores con parámetros
# Un decorador con parámetros recibe argumentos adicionales que pueden modificar su comportamiento. Esto se logra al anidar una función adicional que genera el decorador.

# Estructura de un decorador con parámetros:
def decorador_con_parametros(parametro):
    def decorador(func):
        def wrapper(*args, **kwargs):
            print(f"Parámetro recibido: {parametro}")
            resultado = func(*args, **kwargs)
            print("Después de la función")
            return resultado
        return wrapper
    return decorador

# Ejemplo práctico de un decorador con parámetros:
def mensaje_personalizado(texto):
    def decorador(func):
        def wrapper(*args, **kwargs):
            print(f"Mensaje personalizado: {texto}")
            resultado = func(*args, **kwargs)
            print("Fin del decorador")
            return resultado
        return wrapper
    return decorador

@mensaje_personalizado("Este es un saludo especial")
def saludar(nombre):
    print(f"Hola, {nombre}!")

saludar("Marcos")

