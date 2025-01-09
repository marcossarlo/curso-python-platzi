# **kwargs: Argumentos Nombrados Variables:

# **kwargs permite a una función aceptar un número arbitrario de argumentos nombrados.
# Los argumentos se agrupan en un diccionario donde las claves son los nombres de los parámetros y los valores son sus respectivos valores.

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}: {value}')

print("**kwargs: Argumentos Nombrados Variables:")
print_info(name='Carlos', age=30, city='Bogotá')
print_info(name='Carlos', age=30, city='Bogotá', country = 'Colombia')

print("\nOtro ejemplo:")
def mostrar_datos(**kwargs):
    print("Argumentos nombrados recibidos:")
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

mostrar_datos(nombre="Juan", edad=30, ciudad="Lima")



