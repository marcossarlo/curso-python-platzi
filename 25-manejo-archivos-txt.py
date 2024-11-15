# Clase: Manejo de Archivos .TXT
# https://platzi.com/home/clases/10002-python/70973-manejo-de-archivos-txt/

# En Python, puedes trabajar con archivos de texto (.txt) para leer y escribir datos. Los archivos de texto son una forma común de almacenar información en un formato legible por humanos.

# Leer un archivo linea por linea:
"""with open('cuento.txt', 'r') as file:
    # Leer el contenido del archivo
    for lines in file:
        print(lines.strip())"""
with open('cuento.txt', 'r') as file:
    contenido = file.read()
    print(contenido)

# Leer todas las lineas en una lista
"""with open('cuento.txt', 'r') as file:
    # Leer todas las lineas en una lista
    lines = file.readlines()
    print(lines)"""

# Escribir en un archivo, añadiendo un texto.
"""with open('cuento.txt', 'a') as file:
    file.write("\n\nBy: CHatGPT...")"""

# Sobreescritura de un archivo
"""with open('cuento.txt', 'w') as file:
    file.write("Once upon a time...")"""

# Conteo de las lineas de un archivo
# with open('cuento.txt', 'r') as file:
#     lines = file.readlines()
#     print(f"El archivo tiene {len(lines)} lineas.")
