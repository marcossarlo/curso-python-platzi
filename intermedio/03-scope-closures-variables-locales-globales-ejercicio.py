# Función que recibe una lista de diccionarios
# Cada diccionario tendrá las claves: 
# "name", "age", "salary"

# La función deve devolver una lista de empleados que ganen más de un cierto salario

employeds = [
    {'name': 'Juan', 'age': 45, 'salary': 9500},
    {'name': 'Ana', 'age': 30, 'salary': 4000},
    {'name': 'Luis', 'age': 25, 'salary': 3000}
]

def set_employeds(new_employeds):
    """ 
    Establece la lista global de empleados.

    Args:
        new_employeds (list): Lista de diccionarios con información de los empleados.
    """
    global employeds
    employeds = new_employeds

def get_salary(min_salary):
    """
    Filtra y devuelve una lista de nombres de empleados con un salario mayor o igual al salario mínimo especificado.

    Args:
        min_salary (int): Salario mínimo para filtrar los empleados.

    Returns:
        list: Lista de nombres de empleados que cumplen con el criterio de salario.
    """
    try:
        filtered_employeds = [employed['name'] for employed in employeds if employed['salary'] >= min_salary]
        if filtered_employeds:
            print(f"Empleados con un salario mayor o igual a {min_salary}: {filtered_employeds}")
        else:
            print(f"No hay empleados con un salario mayor o igual a {min_salary}.")
    except KeyError as e:
        print(f"Error: clave no encontrada {e}")
    except TypeError:
        print("Error: tipo de dato incorrecto.")
        return []

# Ejemplo de uso
set_employeds([
    {'name': 'Juan', 'age': 45, 'salary': 9500},
    {'name': 'Marcos', 'age': 45, 'salary': 7500},
    {'name': 'Beto', 'age': 25, 'salary': 3000}
])

get_salary(6000)

