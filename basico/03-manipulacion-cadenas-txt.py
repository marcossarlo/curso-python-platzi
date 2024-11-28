# Asignación de cadenas de texto: " ", ' ', ''' '''.
name = "Marcos"
print(name)

name2 = 'Eduardo'
print(name2)

lastName = '''SarLo
--> Sarmiento Loarte'''
print(lastName)

age = 45

# consultar el tipo de dato de una variable
print(name," -> ", type(name))
print(type(age))

# INDEXACIÓN: propiedades de las cadenas. Las cadenas son colecciones ordenadas y accesibles por índices.
print(name[0])
print(lastName[0])

# Si queremos acceder desde la última posición, se incia con -1
print(lastName[-6])

# Operaciones con cadenas: Concatenación, Repetición
# Concatenación
print(name + " " + name2)
# Repetición
print(name * 5)
print(5 * name2)

# Buenas prácticas
# Si usamos comillas simples enla asignación de una valiable, usar en todas las demás, no usar distintas asignaciones

# Acciones con las cadenas
print(len(name))
print(len(lastName))

# Métodos de las cadenas
nick = "msl"
print(nick + " -> " + nick.upper())

#replace(old, new)
#Reemplaza partes de la cadena.
texto = "hola mundo"
print(texto + " -> " + texto.replace("mundo", "Python"))

#Divide la cadena en una lista según el separador.
texto2 = "hola,mundo,Python"
print(texto2)
print(texto2.split(",")) 

expression = "2 + 3 * 4"
result = eval(expression)  # result será 14
print(result)

# join(iterable)
#Une elementos de una lista  en una sola cadena.
lista = ["hola", "mundo"]
print(lista)
print(" ".join(lista)) 

#find(sub)
#Busca una subcadena y devuelve el índice de su primera aparición.
texto = "hola mundo"
print(texto.find("mundo"))

#startswith(prefix) y endswith(suffix)
#Verifica si la cadena empieza o termina con una subcadena.
texto = "hola world"
print(texto.startswith("hola"))
print(texto.endswith("mundo"))

#Ejemplo Completo:
frase = "  Bienvenido a Python!  "
frase = frase.strip().replace("Python", "el mundo de Python").upper()
print(frase)  # "BIENVENIDO A EL MUNDO DE PYTHON!"

# Listar Métodos para cadenas
#print(dir(str))