# Usando *args y **kwargs Juntos
# En Python, puedes usar *args y **kwargs juntos en una misma función.

class Employee:
    def __init__(self, name, *args, **kwargs):
        self.name = name
        self.skills = args
        self.details = kwargs
    
    def show_employee(self):
        print(f'Employee: {self.name}')
        print('Skills:', self.skills)
        print('Details:s', self.details)

employee = Employee('MarcosSarLo', 'Python', 'JavaScript', 'CSS', age=45, city = 'Huancayo')
employee.show_employee()

print("\nOtro ejemplo:")
print("Puedes usar ambos en la misma función. El orden siempre debe ser: parámetros normales, luego *args y finalmente **kwargs.")
def procesar_datos(requerido, *args, **kwargs):
    print(f"Dato requerido: {requerido}")
    print(f"Otros datos posicionales: {args}")
    print(f"Datos nombrados: {kwargs}")

procesar_datos(
    "Obligatorio",
    1, 2, 3,
    nombre="Ana",
    edad=25,
    ciudad="Cusco"
)