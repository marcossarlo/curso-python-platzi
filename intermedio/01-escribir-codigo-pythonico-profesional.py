#import this

# El zen de Python, por Tim Peters

# Lo bello es mejor que lo feo.
# Lo explícito es mejor que lo implícito.
# Lo simple es mejor que lo complejo.
# Lo complejo es mejor que lo complicado.
# Lo plano es mejor que lo anidado.
# Lo escaso es mejor que lo denso.
# La legibilidad cuenta.
# Los casos especiales no son lo suficientemente especiales como para romper las reglas.
# Aunque la practicidad supera a la pureza.
# Los errores nunca deberían pasar desapercibidos.
# A menos que se silencien explícitamente.
# Ante la ambigüedad, rechace la tentación de adivinar.
# Debe haber una forma obvia (y preferiblemente solo una) de hacerlo.
# Aunque esa forma puede no ser obvia al principio a menos que sea holandés.
# Ahora es mejor que nunca.
# Aunque nunca es a menudo mejor que ahora mismo.
# Si la implementación es difícil de explicar, es una mala idea.
# Si la implementación es fácil de explicar, puede ser una buena idea.
# Los namespace son una idea genial: ¡hagamos más de eso!

# 1. Uso de List Comprehensions
print("1. Uso de List Comprehensions:")
# No Pythonico
nueva_lista = []
for x in range(10):
    nueva_lista.append(x * 2)
print(f"No Pythonico: {nueva_lista}")

# Pythonico
new_list = [x * 2 for x in range(10)]
print(f"Pythonico: {new_list}")

# 2. Desempaquetado de Variables
print("\n2. Desempaquetado de Variables:")
# No Pythonico
punto = (3, 5)
x = punto[0]
y = punto[1]

# Pythonico
x, y = punto
print(x, y)

# 3. Uso de enumerate() y zip()
print("\n3. Uso de enumerate() y zip()")
print("Evita manejar índices manualmente y trabaja con múltiples iterables.")
# No Pythonico
for i in range(len(new_list)):
    #print(i, new_list[i])
    continue
# Pythonico
for i, value in enumerate(new_list):
    print(i, value)

# Ejemplo de uso de zip()
print("Ejemplo de uso de zip()")
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']

# No Pythonico
for i in range(len(list1)):
    #print(list1[i], list2[i])
    continue

# Pythonico
for item1, item2 in zip(list1, list2):
    print(item1, item2)

# 4. Uso de Generadores
print("\n4. Uso de Generadores")
print("Los generadores son más eficientes en memoria que las listas, especialmente con grandes cantidades de datos.")
# Lista (usa más memoria)
numeros = [x * 2 for x in range(10)]
# Generador (usa menos memoria)
numeros_gen = (x * 2 for x in range(10))

# 5. Manejo de Excepciones en Lugar de Condicionales
print("\n5. Manejo de Excepciones en Lugar de Condicionales:\n Python prefiere el enfoque EAFP (Easier to Ask for Forgiveness than Permission).")
# No Pythonico (comprobación explícita)
if 'clave' in diccionario:
    valor = diccionario['clave']

# Pythonico (manejo de excepciones)
try:
    valor = diccionario['clave']
except KeyError:
    valor = None

