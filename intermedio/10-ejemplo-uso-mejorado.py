import csv


class EmployeeManager:
    """Clase para gestionar empleados."""

    def __init__(self):
        """Inicializa la lista de empleados."""
        self.employees = []

    def add_employee(self, name: str, position: str):
        """
        Agrega un empleado a la lista.
        Args:
            name (str): Nombre del empleado.
            position (str): Cargo del empleado.
        """
        if not name.strip():
            raise ValueError("El nombre del empleado no puede estar vacío.")
        if not position.strip():
            raise ValueError("El cargo del empleado no puede estar vacío.")
        
        self.employees.append({"name": name, "position": position})
        print(f"Empleado '{name}' agregado como '{position}'.")

    def remove_employee(self, name: str):
        """
        Elimina un empleado por su nombre.
        Args:
            name (str): Nombre del empleado a eliminar.
        """
        for employee in self.employees:
            if employee["name"] == name:
                self.employees.remove(employee)
                print(f"Empleado '{name}' eliminado.")
                return
        print(f"Empleado '{name}' no encontrado.")

    def list_employees(self):
        """Muestra todos los empleados en la lista."""
        if not self.employees:
            print("No hay empleados registrados.")
            return
        
        print("\nLista de empleados:")
        for i, employee in enumerate(self.employees, start=1):
            print(f"{i}. {employee['name']} - {employee['position']}")

    def search_employee(self, name: str):
        """
        Busca un empleado por su nombre.
        Args:
            name (str): Nombre del empleado a buscar.
        """
        for employee in self.employees:
            if employee["name"] == name:
                print(f"Empleado encontrado: {employee['name']} - {employee['position']}")
                return
        print(f"Empleado '{name}' no encontrado.")

    def export_to_csv(self, file_name: str = "10-ejemplo-employees.csv"):
        """
        Exporta la lista de empleados a un archivo CSV.
        Args:
            file_name (str): Nombre del archivo CSV.
        """
        if not self.employees:
            print("No hay empleados para exportar.")
            return
        
        with open(file_name, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=["name", "position"])
            writer.writeheader()
            writer.writerows(self.employees)
        
        print(f"Lista de empleados exportada a '{file_name}'.")


# Bloque principal para ejecución directa
if __name__ == "__main__":
    manager = EmployeeManager()

    while True:
        print("\nGestión de Empleados")
        print("1. Agregar empleado")
        print("2. Eliminar empleado")
        print("3. Listar empleados")
        print("4. Buscar empleado")
        print("5. Exportar empleados a CSV")
        print("6. Salir")

        try:
            option = int(input("Seleccione una opción: "))
        except ValueError:
            print("Por favor, ingrese un número válido.")
            continue

        if option == 1:
            name = input("Ingrese el nombre del empleado: ").strip()
            position = input("Ingrese el cargo del empleado: ").strip()
            try:
                manager.add_employee(name, position)
            except ValueError as e:
                print(e)
        elif option == 2:
            name = input("Ingrese el nombre del empleado a eliminar: ").strip()
            manager.remove_employee(name)
        elif option == 3:
            manager.list_employees()
        elif option == 4:
            name = input("Ingrese el nombre del empleado a buscar: ").strip()
            manager.search_employee(name)
        elif option == 5:
            manager.export_to_csv()
        elif option == 6:
            print("Saliendo del sistema de gestión de empleados.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")
