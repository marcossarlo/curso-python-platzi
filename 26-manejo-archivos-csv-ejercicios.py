import csv

# Leer un Archivo .csv
file_path = '26-fv_email_addresses.csv'

# Leyendo un .CSV lo devuelve como una LISTA
print('Leyendo un .CSV lo devuelve como una Lista')
try:    
    with open(file_path, mode='r') as file:
        # lee el archivo línea por línea y devuelve cada fila como una lista.
        csv_reader = csv.reader(file)
        # Se recorre el archivo y se imprime cada fila.
        for row in csv_reader:
            print(row)
except FileNotFoundError:
    print(f'El archivo {file_path} no se encuentra en el directorio actual.')
except csv.Error as e:
    print(f"Error al procesar el archivo CSV: {e}")

# Leyendo un .CSV lo devuelve como un DICCIONARIO
# csv.DictReader() es útil si quieres trabajar con archivos .csv que tienen encabezados, ya que devuelve cada fila como un diccionario, con los encabezados como claves.
print('\nLeyendo un .CSV lo devuelve como un Diccionario')
try:
    with open(file_path, mode='r') as file:
        # Se crea un objeto csv_reader que permite leer el archivo.
        csv_reader = csv.DictReader(file)
        # Se recorre el archivo y se imprime cada fila.
        for row in csv_reader:
            print(row)
except FileNotFoundError:
    print(f'El archivo {file_path} no se encuentra en el directorio actual.')
except csv.Error as e:
    print(f"Error al procesar el archivo CSV: {e}")

# Escribir en un Archivo .csv
# Usando csv.writer()
# csv.writer() es útil si quieres escribir en un archivo .csv línea por línea.
print('\nEscribir en un .CSV usando csv.writer()')
emails = [
    ['Nombre', 'Apellido', 'Email'],
    ['Carlos', 'Salazar', 'user1@email.com'],
    ['Julia', 'Montefiory', 'user2@email.com']
]
# Escribir en un archivo CSV
with open('26-salida.csv', 'w', newline='') as file:
    # crea un objeto para escribir en el archivo.
    escritor_csv = csv.writer(file)
    # Escribir cada fila en el archivo CSV
    # escribe varias filas a la vez (usando una lista de listas).
    escritor_csv.writerows(emails)

# Usando csv.DictWriter()
print('\nEscribir en un .CSV usando DictWriter()')
emails_dic = [
    {'Nombre': 'Carlos', 'Apellido': 'Salazar', 'Email': 'user1@emamil.com'},	
    {'Nombre': 'Julia', 'Apellido': 'Montefiory', 'Email': 'user1@emamil.com'},
]
# Escribir en un archivo CSV
with open('26-salida_dict.csv', 'w', newline='') as file:
    fields = ['Nombre', 'Apellido', 'Email']
    escritor_dict = csv.DictWriter(file, fieldnames=fields)
    
    escritor_dict.writeheader()  # Escribir encabezados
    escritor_dict.writerows(emails_dic)

# Otras Funcionalidades del Módulo csv
# Delimitador Personalizado:
print("\nDelimitador Personalizado")
with open(file_path, 'r', newline='') as file:
    lector_csv = csv.reader(file, delimiter=';')  # Usar punto y coma como delimitador
    for fila in lector_csv:
        print(fila)
