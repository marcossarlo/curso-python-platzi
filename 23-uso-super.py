# Clase: Uso de super() en Python
# super() se usa para llamar a métodos de la clase padre
# super() se utiliza para llamar a un método de la clase base (superclase) desde una subclase. Es especialmente útil cuando trabajas con herencia, ya que te permite reutilizar el código de la clase base en la subclase, evitando la duplicación de código.
# ¿Por qué usar super()?
# - Reutilización de Código: Te permite aprovechar el código ya definido en la clase base.
# - Mantenimiento: Facilita el mantenimiento del código al centralizar la lógica común en la clase base.
# - Compatibilidad con Herencia Múltiple: Ayuda a resolver problemas relacionados con la herencia múltiple gracias al Method Resolution Order (MRO).

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello! I am a person.")

class Student(Person):
    def __init__(self, name, age, student_id):
        # super() se usa para llamar al constructor de la clase padre
        super().__init__(name, age)
        self.student_id = student_id

    def greet(self):
        # super() se usa para llamar al método greet() de la clase padre
        super().greet()
        print(f"Hello, my student ID is {self.student_id}")

student = Student("Ana", 20, "S123")
student.greet()


class LivingBeing:
    def __init__(self, name):
        self.name = name

class Person(LivingBeing):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def introduce(self):
        print(f"Hi, I'm {self.name}, {self.age} years old, and my student ID is {self.student_id}")

student = Student("Carlos", 21, "S54321")
student.introduce() 
