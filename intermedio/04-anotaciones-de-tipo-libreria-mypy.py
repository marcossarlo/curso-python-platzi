# Clase: Anotaciones
# https://platzi.com/home/clases/10002-python/71732-anotaciones-de-tipo/

# Instalar la librería mypy
# sudo apt update
# sudo apt install python3-pip
# pip install mypy

#-> al instalar salió una advertencia:
# WARNING: The script mypy is installed in '/home/usuario/.local/bin' which is not on PATH.
#-> al ejecutar salió error:

#Solución:
# Parece que mypy no está en tu PATH. Para solucionarlo, puedes agregar el directorio donde se instaló mypy a tu PATH. 
# 1. nano ~/.bashrc
# 2. Agrega la siguiente línea al final del archivo: export PATH="$PATH:/home/usuario/.local/bin"
# 3. Guarda los cambios y cierra el archivo.
# 4. Ejecuta source ~/.bashrc para aplicar los cambios.
# 5. Ahora, mypy debería estar en tu PATH y podrás ejecutarlo desde cualquier lugar.

# Ejecutar: mypy 04-anotaciones-de-tipo.py
# Success: no issues found in 1 source file
