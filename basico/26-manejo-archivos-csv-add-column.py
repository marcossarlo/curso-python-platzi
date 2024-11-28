import csv

file_path = '26-products.csv'
updated_file_path = '26-products_updated.csv'

with open(file_path, mode='r') as file:
    csv_reader = csv.DictReader(file)
    # Obtener los nombres de las columnas existentes y agregar dos nuevas columnas
    fieldnames = csv_reader.fieldnames + ['total_value', 'discounted_price']

    with open(updated_file_path, mode='w', newline='') as updated_file:
        csv_writer = csv.DictWriter(updated_file, fieldnames=fieldnames)
        csv_writer.writeheader()  # Escribir los encabezados

        for row in csv_reader:
            row['total_value'] = float(row['price']) * int(row['quantity'])
            row['discounted_price'] = float(row['price']) * 0.9  # Ejemplo de precio con descuento del 10%
            csv_writer.writerow(row)