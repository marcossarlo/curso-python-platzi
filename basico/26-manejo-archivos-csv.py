# Clase: Manejo de Archivos CSV (CLASE NUEVA)
# https://platzi.com/home/clases/10002-python/70974-manejo-de-archivos-csv/

# En Python, puedes trabajar con archivos CSV (Comma Separated Values) para leer y escribir datos tabulares. Los archivos CSV son una forma común de almacenar información en un formato legible por humanos y máquinas.

# Leer un archivo CSV con DictReader
import csv
# with open("26-products.csv", mode="r") as file:
#     csv_reader = csv.DictReader(file)
#     for row in csv_reader:
#         print(row)

# Mostrar la información por columnas
# with open("26-products.csv", mode="r") as file:
#     csv_reader = csv.DictReader(file)
#     for row in csv_reader:
#         print(f"Producto: {row['name']}, Precio: {row['price']}")

# Agregar nuevo producto en el archivo CSV
new_product = {
    'name': 'Wireless Charger',
    'price': 175,
    'quantity': 10,
    'brand': 'Sony ChargerMaster',
    'category': 'Accessories',
    'entry_date': '2024-09-01'
}

with open('26-products.csv', mode='a', newline='') as file:
    file.write('\n')
    csv_writer = csv. DictWriter(file, fieldnames = new_product.keys())
    csv_writer.writerow(new_product)