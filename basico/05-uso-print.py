# Todo lo que Debes Saber sobre print en Python
# Clase: https://platzi.com/home/clases/10002-python/70199-todo-lo-que-debes-saber-sobre-print-en-python/
print('Nunca pares de aprender') 

# Uso de la coma en print, Python añade automáticamente un espacio entre los argumentos. Esto es diferente a concatenar cadenas con el operador +
print("\n")
print("-> Uso de la coma en print, Python añade automáticamente un espacio entre los argumentos. Esto es diferente a concatenar cadenas con el operador +")
print('Nunca', 'pares', 'de', 'aprender') 
print("Nunca" + "pares" + "de" + "aprender")
print("Nunca" + " " + "pares" + " " + "de" + " " + "aprender")

# Uso de SEP
print("\n")
print("-> Uso de SEP")
print('Nunca', 'pares', 'de', 'aprender', sep='_-_')

# Uso de END: asegura que se impriman en la misma línea
print("\n")
print("-> Uso de END: asegura que se impriman en la misma línea")
print('Nunca', 'pares', end='___')
print('de', 'aprender')

# Impresión de variables
print("\n")
print("-> Impresión de variables")
frase = "Nunca pares de aprender"
author = "Platzi"
print("Frase:", frase + "\n" + "Autor:", author)


# F-STRINGS
# permiten insertar expresiones dentro de cadenas de texto
print("\n")
print("-> F-STRINGS: permiten insertar expresiones dentro de cadenas de texto")
frase = "Nunca pares de aprender"
author = "Platzi"
print(f"Frase: {frase} | Autor: {author}")

# FORMAT
print("\n")
print("-> FORMAT")
frase = "Nunca pares de aprender"
author = "Platzi"
print("Frase: {} | Autor: {}".format(frase, author))

valor = 3.14559
print("Valor: {:.2f}".format(valor))

# Caracteres especiales
print("\n")
print("-> Caracteres especiales")
print('Hola soy \"MarcosSarLo\'')
print("La ruta de archivo es: C:\\Users\\Usuario\\Desktop\\archivo.txt")