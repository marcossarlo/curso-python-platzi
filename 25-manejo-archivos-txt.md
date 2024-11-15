# Clase: Manejo de Archivos .TXT
https://platzi.com/home/clases/10002-python/70973-manejo-de-archivos-txt/

El manejo de archivos .txt en Python es una tarea común y esencial que te permite leer y escribir datos en archivos de texto. Python facilita este proceso utilizando la función incorporada ```open()```. Aquí te explico cómo manejar archivos .txt de manera sencilla.

## Apertura de Archivos con open()
La función open() se utiliza para abrir un archivo y devuelve un objeto de archivo que puedes usar para interactuar con él.
```
archivo = open('nombre_archivo.txt', modo)
```

## Modos de Apertura
| Modo   | descripción |
|--------|-----------|
| 'r'    | Leer (por defecto). Da error si el archivo no existe.    |
| 'w'    | Escribir. Crea un archivo nuevo o sobrescribe si existe.    |
| 'a'    | Añadir. Escribe al final del archivo sin sobrescribir.    |
| 'r+'   | Leer y escribir desde el principio.    |
| 'b'    | Modo binario (para archivos no de texto).    |

### Ejemplos prácticos
```python
# Abrir archivo en modo lectura
with open('datos.txt', 'r') as archivo:
    contenido = archivo.read()
    print(contenido)
# Utilizamos with open(...) as ... para abrir el archivo. Esto asegura que el archivo se cierre automáticamente al terminar.
# archivo.read() lee todo el contenido del archivo como una cadena.

# Leer línea por línea
with open('datos.txt', 'r') as archivo:
    for linea in archivo:
        print(linea.strip())  # strip() elimina los saltos de línea

# Escribir en un Archivo ('w')
# Si el archivo no existe, se creará. Si existe, sobrescribirá su contenido.
with open('nueva_info.txt', 'w') as archivo:
    archivo.write("Primera línea\n")
    archivo.write("Segunda línea\n")

# Añadir Contenido a un Archivo ('a')
# El modo 'a' (append) permite añadir contenido al final del archivo sin eliminar lo anterior.
with open('nueva_info.txt', 'a') as file:
    file.write("Línea adicional\n")

# Leer y Escribir ('r+')
# Este modo te permite leer y escribir en un archivo existente.
with open('nueva_info.txt', 'r+') as archivo:
    print(archivo.read())  # Leer el contenido existente
    archivo.write("Nueva línea añadida\n")  # Añadir al final
```

## Métodos Comunes para Archivos
| Modo   | descripción |
|--------|-----------|
| read() | Lee todo el archivo como una sola cadena. |
| readline() | Lee una sola línea. |
| readlines() | Lee todas las líneas y las devuelve en una lista. |
| write(cadena) | Escribe una cadena en el archivo. |
| writelines(lista) | Escribe una lista de cadenas en el archivo. |
| close() | Cierra el archivo (no es necesario con with). |

### Ejemplos
```python
# Copiar el Contenido de un Archivo a Otro
# Leer desde 'datos.txt' y escribir en 'copia.txt'
with open('datos.txt', 'r') as archivo_lectura:
    contenido = archivo_lectura.read()

with open('copia.txt', 'w') as archivo_escritura:
    archivo_escritura.write(contenido)

# Verificar si un Archivo Existe
# Para evitar errores al intentar abrir un archivo que podría no existir, puedes usar el módulo os o pathlib.
from pathlib import Path

archivo = Path('datos.txt')
if archivo.exists():
    print("El archivo existe")
else:
    print("El archivo no existe")

# Uso de try-except para Manejo de Errores
try:
    with open('inexistente.txt', 'r') as archivo:
        print(archivo.read())
except FileNotFoundError:
    print("El archivo no fue encontrado.")
```

## Resumen
- Usa with open() para asegurar el cierre automático del archivo.
- Modos: 'r' para leer, 'w' para escribir (sobrescribe), 'a' para añadir.
- Métodos útiles: read(), write(), readline(), readlines().
- Siempre maneja posibles errores usando try-except.