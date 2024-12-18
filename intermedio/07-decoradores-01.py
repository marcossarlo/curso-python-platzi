# Clase: Decoradores
# https://platzi.com/home/clases/10002-python/71735-decoradores-en-python/

# Un decorador en Python es una función que modifica el comportamiento de otra función o método. 
# Permiten "envolver" una función para añadirle funcionalidades adicionales sin alterar su estructura original. 
# Son especialmente útiles para reutilizar código y separar preocupaciones.
# Un decorador es una función que toma otra función como argumento y devuelve una nueva función.
# Para definir un decorador, se utiliza la sintaxis @decorador encima de la función que se desea decorar.

def log_transaction(func):
    def wrapper(*args, **kwargs):
        print('1. Log de la transacción...')
        func(*args, **kwargs)
        print('3. Log terminado...')
    return wrapper
        
@log_transaction
def process_payment():
    print('2. Procesando pago....')

print("Decorador 1:")
process_payment()

# Ejemplo 2
def decorador(func):
    def wrapper(*args, **kwargs):
        print("Antes de ejecutar la función")
        resultado = func(*args, **kwargs)
        print("Después de ejecutar la función")
        return resultado
    return wrapper

@decorador
def saludar(nombre):
    print(f"Hola, {nombre}!")

print("\nDecorador 2:")
saludar("Marcos")
