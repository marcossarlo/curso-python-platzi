# Juego de Piedra, Papel o Tijera
print("¡Juego de Piedra, Papel o Tijera!")
# Opciones del juego
options = ["piedra", "papel", "tijera"]

print("Elige una opción: piedra, papel o tijera")

# Entrada de los jugadores
gamer1 = input("Jugador 1: ").lower()
gamer2 = input("Jugador 2: ").lower()
# print("Jugador 1: ", gamer1)
# print("Jugador 2: ", gamer2)

# Verificar que la elección sea válida
if gamer1 not in options or gamer2 not in options:
    print("Elección inválida. Intenta de nuevo")
    exit()

if gamer1 == gamer2:
    print("Es un Empate")
# Condiciones donde el jugador 1 gana
elif (gamer1 == "piedra" and gamer2 == "tijera") or \
     (gamer1 == "tijera" and gamer2 == "papel") or \
     (gamer1 == "papel" and gamer2 == "piedra"):
    print("Jugador 1 Gana el juego")
else:
    print("Jugador 2 Gana el juego")

    

