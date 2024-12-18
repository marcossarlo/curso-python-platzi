# Clase: Decoradores
# https://platzi.com/home/clases/10002-python/71735-decoradores-en-python/

def check_and_log_access(file_name):
    def decorator(func):
        def wrapper(employee):
            action = f"Empleado: {employee['name']}, Rol: {employee['role']}, Acción: {func.__name__}"
            if employee.get('role') == 'admin':
                # Registrar la acción en el archivo de texto
                with open(file_name, 'a') as file:
                    file.write(f"{action} - ACCIÓN REALIZADA\n")
                return func(employee)
            else:
                # Registrar el acceso denegado en el archivo de texto
                with open(file_name, 'a') as file:
                    file.write(f"{action} - ACCESO DENEGADO\n")
                print('ACCESO DENEGADO. Solo los administradores pueden acceder.')
        return wrapper
    return decorator

@check_and_log_access('07-employee_actions.txt')
def delete_employee(employee):
    print(f"El empleado {employee['name']} ha sido eliminado.")

admin = {'name': 'Carlos', 'role': 'admin'}
employee = {'name': 'Ana', 'role': 'employee'}
employee1 = {'name': 'Nik', 'role': 'subadmin'}
admin2 = {'name': 'Coverdale', 'role': 'admin'}

print('Uso del decorador check_and_log_access:')
delete_employee(employee1)