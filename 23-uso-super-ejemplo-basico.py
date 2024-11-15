# Clase: Uso de super() en Python
# super() se usa para llamar a métodos de la clase padre
# super() se utiliza para llamar a un método de la clase base (superclase) desde una subclase. Es especialmente útil cuando trabajas con herencia, ya que te permite reutilizar el código de la clase base en la subclase, evitando la duplicación de código.
# ¿Por qué usar super()?
# - Reutilización de Código: Te permite aprovechar el código ya definido en la clase base.
# - Mantenimiento: Facilita el mantenimiento del código al centralizar la lógica común en la clase base.
# - Compatibilidad con Herencia Múltiple: Ayuda a resolver problemas relacionados con la herencia múltiple gracias al Method Resolution Order (MRO).

# Supongamos que estamos desarrollando un sistema para gestionar diferentes tipos de empleados. Tenemos una clase base Empleado y una subclase Gerente.

class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def mostrar_info(self):
        return f"Empleado: {self.nombre}, Salario: {self.salario}"

class Gerente(Empleado):
    def __init__(self, nombre, salario, departamento):
        # Usamos super() para llamar al constructor de la clase base
        super().__init__(nombre, salario)
        self.departamento = departamento

    def mostrar_info(self):
        # Usamos super() para reutilizar el método mostrar_info() de la clase base
        info_base = super().mostrar_info()
        return f"{info_base}, Departamento: {self.departamento}"

# Uso
gerente = Gerente("Marcos", 5000, "TI")
print(gerente.mostrar_info())  # Salida: Empleado: Marcos, Salario: 5000, Departamento: TI
