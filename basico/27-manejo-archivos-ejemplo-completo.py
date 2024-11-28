# Manejo de Archivos JSON

# Ejemplo Completo: Trabajar con JSON en un Proyecto
# Supongamos que tienes una lista de productos en un archivo JSON y quieres cargarla, agregar un nuevo producto, y guardarla.
import json

path_file = '27-ejemplo-completo.json'
# Cargar productos
with open(path_file, 'r') as file:
    products = json.load(file)

# Agregar un nuevo producto
new_product = {"id": 3, "nombre": "Monitor", "precio": 150}
products.append(new_product)

# Guardar cambios
with open(path_file, 'w') as file:
    json.dump(products, file, indent=4)

# Mostrar los productos actualizados
print("Productos actualizados:")
for product in products:
    print(f"{product['nombre']} - ${product['precio']}")
