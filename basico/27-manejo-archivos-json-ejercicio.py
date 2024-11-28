# Ejercicio:
# Leer un archivo CSV y convertirlo a un archivo JSON.
import csv
import json

csv_file_path = '27-ejercicio.csv'
json_file_path = '27-ejercicio.json'

# Leer el archivo CSV y almacenar los datos en una lista de diccionarios
data = []
with open(csv_file_path, mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        data.append(row)


# Escribir los datos en un archivo JSON
with open(json_file_path, mode='w') as json_file:
    json.dump(data, json_file, indent=4)

print(f"Archivo convertido de {csv_file_path} a {json_file_path}")

# Leer el archivo JSON y mostrar los datos
with open(json_file_path, mode='r') as json_file:
    data = json.load(json_file)
    print("\nDatos del archivo JSON:")
    for row in data:
        print(row)

# Leer un archivo JSON y convertirlo a un archivo CSV:
json_file_path = '27-ejercicio2.json'
csv_file_path = '27-ejercicio2.csv'

# Leer el archivo JSON y almacenar los datos en una lista de diccionarios
data = []
with open(json_file_path, mode='r') as json_file:
    data = json.load(json_file)

# Obtener los nombres de las columnas (keys) del primer diccionario
fieldnames = data[0].keys()

# Escribir los datos en un archivo CSV
with open(csv_file_path, mode='w', newline='') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()
    csv_writer.writerows(data)

print(f"Archivo convertido de {json_file_path} a {csv_file_path}")

# Leer el archivo CSV y mostrar los datos
with open(csv_file_path, mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    print("\nDatos del archivo CSV:")
    for row in csv_reader:
        print(row)

