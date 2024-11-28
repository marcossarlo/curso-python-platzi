# Clase: Uso de super() en Python
# super() se usa para llamar a métodos de la clase padre
# super() se utiliza para llamar a un método de la clase base (superclase) desde una subclase. Es especialmente útil cuando trabajas con herencia, ya que te permite reutilizar el código de la clase base en la subclase, evitando la duplicación de código.
# ¿Por qué usar super()?
# - Reutilización de Código: Te permite aprovechar el código ya definido en la clase base.
# - Mantenimiento: Facilita el mantenimiento del código al centralizar la lógica común en la clase base.
# - Compatibilidad con Herencia Múltiple: Ayuda a resolver problemas relacionados con la herencia múltiple gracias al Method Resolution Order (MRO).

# Cuando tienes herencia múltiple, super() sigue el orden de resolución de métodos, conocido como MRO (Method Resolution Order). Esto asegura que los métodos se llamen en el orden correcto, evitando problemas de duplicación.
class A:
    def metodo(self):
        print("Método de A")

class B(A):
    def metodo(self):
        print("Método de B")
        super().metodo()

class C(A):
    def metodo(self):
        print("Método de C")
        super().metodo()

class D(B, C):
    def metodo(self):
        print("Método de D")
        super().metodo()

# Uso
obj = D()
obj.metodo()
print(D.__mro__)

# Resumen
# . super() es útil para reutilizar métodos de la clase base, especialmente en la inicialización de atributos.
# . Facilita el uso de herencia múltiple, asegurando que los métodos se llamen en el orden correcto según el MRO.
# . Mejora la mantenibilidad y legibilidad del código al evitar duplicaciones.

# super() es una herramienta poderosa que te ayuda a aprovechar al máximo la herencia en Python, permitiendo que tu código sea más limpio y eficiente.