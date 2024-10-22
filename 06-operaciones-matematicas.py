# Operaciones Matemáticas en Python
# https://platzi.com/home/clases/10002-python/70084-operadores/
number1 = 10
number2 = 5

print("Operaciones Matemáticas en Python:")
print(f"Suma {number1} + {number2}:", number1 + number2)
print(f"Resta {number1} - {number2}:", number1 - number2)
print(f"Multiplicación {number1} * {number2}:", number1 * number2)
print(f"División {number1} / {number2}:", number1 / number2)
print(f"División Entera {number1} // {number2}:", number1 // number2)
print(f"Módulo {number1} % {number2}:", number1 % number2)
print(f"Potencia {number1} ** {number2}:", number1 ** number2)
print(f"Raíz cuadrada de {number1}:", number1 ** 0.5) 
print(f"Raíz cúbica de {number1}:", number1 ** (1/3)) 

# Operadores de Asignación
print("\n")
print("Operadores de Asignación")
number3 = 10
number3 += 5
number3 -= 5
number3 *= 5
number3 /= 5
number3 //= 5
number3 %= 5
number3 **= 5
print(number3)

# ¿Qué es PEMDAS y cómo afecta nuestras operaciones?
print("\n")
print("PEMDAS:")
print("Es la regla de prioridad de operaciones: ")
print("Paréntesis, Exponentes, Multiplicación y División, Adición y Sustracción")
operation1 = 3 + 2 * 5
print("3 + 2 * 5 = ", operation1)

operation2 = (3 + 2) * 5
print("(3 + 2) * 5 = ", operation2)

operation3 = (2+3) * (4**2) / 8 - 1
print("(2+3) * (4**2) / 8 - 1 = ", operation3)
operation4 = (2+3) * (4**2) / (8 - 1)
print("(2+3) * (4**2) / (8 - 1) = ", operation4)

# Operadores Booleanos
print("\n")
print("Operadores Booleanos")
a = 10
b = 5
print(f"{a} > {b}: ", a > b)
print(f"{a} < {b}: ", a < b)
print(f"{a} >= {b}: ", a >= b)
print(f"{a} <= {b}: ", a <= b)
print(f"{a} == {b}: ", a == b)
print(f"{a} != {b}: ", a != b)





