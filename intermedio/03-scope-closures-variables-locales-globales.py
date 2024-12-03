# Clase: Scope y closures: variables locales y globales
# https://platzi.com/home/clases/10002-python/71731-scope-y-closures-variables-locales-y-globales/

# En Python, las variables pueden ser locales o globales, dependiendo de dónde se definen. El alcance de una variable determina en qué partes del código puede ser utilizada.

# 1. Variables Locales
# Las variables definidas dentro de una función son locales y solo pueden ser accedidas desde esa función. Si intentas acceder a una variable local desde fuera de la función, Python lanzará un error.
# Ejemplo:
# """
def suma(a, b):
    resultado = a + b # Variable local
    return f"El resultado de la suma es {resultado}"

print(suma(5, 3))  # 8
#print(resultado)  # NameError: name 'resultado' is not defined

# 2. Variables Globales
# Las variables definidas fuera de una función son globales y pueden ser accedidas desde cualquier parte del código. Sin embargo, si intentas modificar una variable global dentro de una función, Python creará una nueva variable local con el mismo nombre, en lugar de modificar la variable global.
# Ejemplo:
x = 100 # Variable global
def show_global():
    print(f"El valor de x es {x}")

show_global()  # 100

y = "Global" # Variable global
def outer_funtion():
    y = "Enclosing"
    # función interna
    def inner_function():
        y = "Local"
        print(y)
    
    inner_function()
    print(y)

outer_funtion()  # Local, Enclosing
print(y)

# 3. Palabras Clave global y nonlocal
print("\n3. Palabras Clave global y nonlocal")
# Para modificar una variable global dentro de una función, puedes utilizar la palabra clave global seguida del nombre de la variable.
# Ejemplo:
z = 10 # Variable global
def modify_global():
    global z
    z = 20
    print(f"El valor de z dentro de la función es {z}")

modify_global()
print(z)  # 20

# Para modificar una variable de una función externa en una función interna, puedes utilizar la palabra clave nonlocal seguida del nombre de la variable.
# Ejemplo:
def outer_function():
    a = 5
    def inner_function():
        nonlocal a
        a = 10
        print(f"El valor de a dentro de la función interna es {a}")
    
    inner_function()
    print(f"El valor de a fuera de la función interna es {a}")

outer_function()


