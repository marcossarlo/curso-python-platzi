# MODÚLO: Funciones y Manejo de Excepciones en PytHON
# CLASE: Uso de Funciones en Python
# https://platzi.com/home/clases/10002-python/70189-definicion-y-uso-de-funciones/

def greet(name="[Sin nombre]", last_name="[Sin apellido]"):
    print("Hola", name, last_name)

# greet("Marcos", "Sarlo")
# greet("Marcos")
# greet()
# greet(last_name="Sarlo", name="Marcos")

def add(a, b):
    return a + b

def substraction(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def calculator():
    options = ["1", "2", "3", "4", "5"]
    while True:
        print("\nOpciones:")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Salir")
        
        option = input("\nIngresa una opción (1, 2, 3, 4, 5): ")
        if option not in options:
            print("Opción no válida, intenta de nuevo")
            continue
        if option == "5":
            print("¡Hasta luego!")
            break
        num1=float(input("Ingresa el primer número: "))
        num2=float(input("Ingresa el segundo número: "))
        if option == "1":
            print("Resultado de la suma es: ", add(num1, num2))
        elif option == "2":
            print("Resultado de la resta es: ", substraction(num1, num2))
        elif option == "3":
            print("Resultado de la multiplicación es: ", multiply(num1, num2))
        else:
            if num2 == 0:
                print("No se puede dividir por cero")
                continue
            print("Resultado de la división es: ", divide(num1, num2))

calculator()

