# MÓDULO: Control de Flujo en Python
# CLASE: Estructuras condicionales
# https://platzi.com/home/clases/10002-python/70090-estructuras-condicionales/

# Estructuras condicionales
# Las estructuras condicionales nos permiten tomar decisiones en nuestro código, ejecutando un bloque de código si se cumple una condición y otro bloque si no se cumple.
# En Python, las estructuras condicionales se definen con la palabra reservada if, seguida de la condición a evaluar y dos puntos (:). Si la condición se cumple, se ejecuta el bloque de código que está a continuación. Para evaluar más de una condición, se pueden usar las palabras reservadas elif y else.

x = 9
if x > 10:
    print(x, "es mayor que 10")
elif x == 10:
    print(x, "es igual a 10")
else:
    print(x, "es menor que 10")

# ¿Cómo se manejan múltiples condiciones en un solo IF?
# Para evaluar múltiples condiciones en un solo if, se pueden usar los operadores lógicos and y or. El operador and evalúa si dos condiciones son verdaderas, mientras que el operador or evalúa si al menos una de las condiciones es verdadera.
print("\n")
print("¿Cómo se manejan múltiples condiciones en un solo IF?")
x = 10
y = 3
if x > 5 and y > 15:
    print("x es mayor que 5 y y es mayor que 15")
if x > 5 or y > 15:
    print("x es mayor que 5 o y es mayor que 15") 

# ¿Qué es la negación en las condiciones?
# La negación en las condiciones se puede hacer con el operador not. Este operador invierte el valor de verdad de una condición, es decir, si la condición es verdadera, la negación la vuelve falsa y viceversa.
print("\n")
print("¿Qué es la negación en las condiciones?")
x = 15
if not x == 5:
    print(x, "no es igual a 5")
else:
    print(x, "es igual a 5")

# ¿Cómo se anidan las estructuras IF?
# Las estructuras if se pueden anidar, es decir, se pueden colocar unas dentro de otras. Esto permite evaluar múltiples condiciones de forma jerárquica.
print("\n")
print("¿Cómo se anidan las estructuras IF?")
x = 1
y = 6
if x > 5:
    if y > 5:
        print("X y Y son mayores que 5")
    else:
        print("X es mayor que 5 pero Y no lo es")
elif y > 5:
    print("Y es mayor que 5 pero X no lo es")
else:
    print("Ni X ni Y son mayores que 5")
    


