# *args: Argumentos Posicionales Variables:

# *args se usa cuando no sabemos cuantos argumentos se van a pasar a la función
# *args se usa para pasar una lista de argumentos a una función
# *args se usa para pasar un número variable de argumentos a una función
# *args es una tupla, no es mutable
# *args es una lista de argumentos

print("*args: Argumentos Posicionales Variables")
def sum_numbers(*args):
    return sum(args)

print(sum_numbers(1,2,3,4,5))
print(sum_numbers(1,2))
print(sum_numbers(1,2,3,4,5,7,8,9,10))

# /*/*/*/*/*/
print("\notro ejemplo:")
def suma(*args):
    total = sum(args)  # Los argumentos posicionales se tratan como una tupla
    print(f"Argumentos recibidos: {args}")
    return f"suma total: {total}"

print(suma(1, 2, 3))  # 6
print(suma(4, 5, 6, 7))  # 22
