# Desempaquetado con * y ** en Python

# Puedes usar * para desempaquetar una lista o tupla y ** para un diccionario al llamar funciones.

# El desempaquetado en Python se refiere a la técnica que permite enviar elementos de una colección (como listas o diccionarios) como argumentos en funciones.

# Para las funciones que usan *args, puedes pasar una lista y descomponerla en argumentos individuales. 
# Con **kwargs, haces lo mismo pero con diccionarios.


#Desempaquetado args
def add(a, b, c):
    return a + b + c

def show_info(name, age):
    print(f"Name: {name}, Age: {age}")

values = (1, 2, 3)
data = {"name": "Ana", "age": 28}

print(add(*values)) 
show_info(**data)

print("\nOtro ejemplo:")
def saludar(nombre, edad):
    print(f"Hola, {nombre}. Tienes {edad} años.")

# Desempaquetar tupla
datos = ("Pedro", 28)
saludar(*datos)

# Desempaquetar diccionario
datos_dict = {"nombre": "María", "edad": 32}
saludar(**datos_dict)
