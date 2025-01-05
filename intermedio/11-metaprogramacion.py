# La metaprogramación en Python se refiere a escribir código que manipula o modifica otros fragmentos de código o incluso a sí mismo, ya sea durante la ejecución o antes de ser ejecutado. Esto permite crear programas más dinámicos y flexibles. En Python, la metaprogramación se logra mediante conceptos como decoradores, metaclases, introspección y la manipulación de atributos de clases y objetos.


class MultiplierFactory:
    
    def __new__(cls, factor: int):
        print(f"Creando instancia con factor {factor}")
        return super(MultiplierFactory, cls).__new__(cls)
    
    def __init__(self, factor: int):
        print(f"Inicializando con factor {factor}")
        self.factor = factor
    
    def __call__(self, number: int) -> int:
        return number * self.factor
    
multiplier = MultiplierFactory(5)

result = multiplier(10)
print(result)

# Ventajas de la Metaprogramación:
# Flexibilidad: Permite crear estructuras de código dinámicas y reutilizables.
# Reducir repetición: Los decoradores y metaclases simplifican patrones repetitivos.
# Automatización: Ayuda a construir herramientas y frameworks más automatizados, como Django o Flask.

# Desventajas de la Metaprogramación:
# Complejidad: Puede hacer el código difícil de entender y depurar.
# Riesgo de errores: La manipulación dinámica puede generar errores difíciles de detectar.
# Rendimiento: Puede introducir sobrecarga si no se usa adecuadamente.
