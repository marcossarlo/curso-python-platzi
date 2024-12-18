# Clase: Decoradores
# https://platzi.com/home/clases/10002-python/71735-decoradores-en-python/

def check_access(func):
    def wrapper(employee):
        # Comprobar si el empleado tiene rol 'admin'
        if employee.get('role') == 'admin':
            return func(employee)
        else:
            print('ACCESO DENEGADO. Solo los administradores pueden acceder.')
    return wrapper
        
@check_access
def delete_employee(employee):
    print(f"Elempleado {employee['name']} ha sido eliminado.")

admin = {'name': 'Carlos', 'role': 'admin'}
employee = {'name': 'Ana', 'role': 'employee'}

print('Ejemplo 1')
delete_employee(admin)
#delete_employee(employee)

# Ejemplo 2
def require_permission(user):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if user == "admin":
                print("Permiso concedido")
                return func(*args, **kwargs)
            else:
                print("Permiso denegado")
                return None
        return wrapper
    return decorator

@require_permission(user="admin")
def eliminar_usuario(usuario_id):
    print(f"Usuario {usuario_id} eliminado")

print("\nEjemplo 2")
eliminar_usuario(101)

# Ejemplo 3
def contador_llamadas(func):
    llamadas = 0
    def wrapper(*args, **kwargs):
        nonlocal llamadas
        llamadas += 1
        print(f"\nLlamada número: {llamadas}")
        return func(*args, **kwargs)
    return wrapper

@contador_llamadas
def saludar(nombre):
    print(f"Hola, {nombre}!")

print("\nEjemplo 3")
saludar("Marcos")
saludar("Ana")
saludar("Nik")

