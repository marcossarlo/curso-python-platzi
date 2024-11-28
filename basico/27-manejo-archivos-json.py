# Manejo de Archivos JSON
# https://platzi.com/home/clases/10002-python/70975-manejo-de-archivos-json/


import json

file_path = '27-products.json'

try:
    with open(file_path, mode='r') as file:
        products = json.load(file)
        for product in products:
            #print(product)
            print(f"Product: {product['name']}, Price: {product['price']}")
except FileNotFoundError:
    print(f'El archivo {file_path} no se encuentra en el directorio actual.')
except json.JSONDecodeError as e:
    print(f"Error al procesar el archivo JSON: {e}")
    

