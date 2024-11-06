# MODÚLO: Funciones y Manejo de Excepciones en PytHON
# CLASE: Manejo de Excepciones y Uso de Pass (CLASE NUEVA)
# https://platzi.com/home/clases/10002-python/70971-manejo-de-excepciones-y-uso-de-pass/

# Las excepciones en Python están organizadas en una jerarquía de clases, donde las excepciones más generales se encuentran en la parte superior y las más específicas en la parte inferior.
# Esta organización jerárquica permite a los programadores manejar excepciones de manera más precisa y efectiva.

# try-except:
# Las excepciones en Python se pueden manejar con la declaración try-except.
# La declaración try-except permite a los programadores capturar excepciones y manejarlas de manera adecuada.
# La declaración try-except se compone de dos bloques: el bloque try y el bloque except.
# El bloque try contiene el código que puede generar una excepción.
# El bloque except contiene el código que maneja la excepción.
# La declaración try-except se utiliza para manejar excepciones y evitar que el programa se detenga.
# Las excepciones en Python se pueden manejar de manera individual o en grupos.
# Las excepciones en Python se pueden manejar de manera genérica o específica.
# Las excepciones en Python se pueden manejar de manera anidada o encadenada.

# try-except-finally:
# Las excepciones en Python se pueden manejar con la declaración try-except-finally.
# La declaración try-except-finally permite a los programadores ejecutar un bloque de código después de manejar una excepción.
# La declaración try-except-finally se compone de tres bloques: el bloque try, el bloque except y el bloque finally.
# El bloque finally se ejecuta siempre, independientemente de si se genera una excepción o no.

# try-except-else-finally:
# Las excepciones en Python se pueden manejar con la declaración try-except-else.
# La declaración try-except-else permite a los programadores ejecutar un bloque de código si no se genera una excepción.
# La declaración try-except-else se compone de cuatro bloques: el bloque try, el bloque except, el bloque else y el bloque finally.
# El bloque else se ejecuta si no se genera una excepción.
# Ejemplos usando try-except-else:
try:
    print("\nEjemplos usando try-except-else-finally")
    dividend = int(input("Ingresa un número dividendo: "))
    divisor = int(input("Ingresa un número divisor: "))
    print(f"Resultado: {dividend/divisor}") 
except ZeroDivisionError:
    print("No se puede dividir por cero.")
except ValueError:
    print("Por favor, ingresa un número entero válido.")
else:
    print("La división se realizó correctamente.")
finally:
    print("--> Fin del programa <--")


# raise:
# Las excepciones en Python se pueden manejar con la declaración raise.
# La declaración raise permite a los programadores generar una excepción de forma manual.
# La declaración raise se utiliza para lanzar excepciones personalizadas.
# Ejemplos usando raise:
try:
    print("\nEjemplos usando raise")
    number = float(input("Ingresa un número: "))
    if number < 0:
        raise ValueError("No se puede ingresar un número negativo.")
    print(f"El número ingresado es: {number}")
except ValueError as error:
    print("Error:", error)
finally:
    print("--> Fin del programa <--")

# assert:
# Las excepciones en Python se pueden manejar con la declaración assert.
# La declaración assert permite a los programadores verificar si una condición es verdadera.
# La declaración assert se utiliza para realizar pruebas de forma automática.
# Ejemplo usando assert:
try:
    print("\nEjemplo usando assert")
    number = int(input("Ingresa un número: "))
    assert number >= 0, "No se puede ingresar un número negativo."
    print(f"El número ingresado es: {number}")
except AssertionError as a_error:
    print("Error:", a_error)
except ValueError as v_error:
    print("Error:", v_error)
finally:
    print("--> Fin del programa <--")
    
# pass:
# Las excepciones en Python se pueden manejar con la declaración pass.
# La declaración pass permite a los programadores crear bloques de código vacíos.
# La declaración pass se utiliza para indicar que no se requiere ninguna acción.
# La declaración pass se utiliza para evitar errores de sintaxis.
# Ejemplo usando pass:
try:
    print("\nEjemplo usando pass")
    number = int(input("Ingresa un número: "))
    if number < 0:
        raise ValueError("No se puede ingresar un número negativo.")
    print(f"El número ingresado es: {number}")
except ValueError as error:
    pass
finally:
    print("--> Fin del programa <--")


