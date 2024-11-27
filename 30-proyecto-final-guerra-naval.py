BOARD_SIZE = 10
EMPTY_CELL = ' '
HIT_CELL = 'T'
MISS_CELL = 'A'

class Ship:
    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size
        self.positions = []
        self.hits = 0

    def place_ship(self, start_row: int, start_col: int, direction: str, board: list) -> bool:
        positions = []
        if direction == 'H':
            if start_col + self.size > BOARD_SIZE:
                return False
            for i in range(self.size):
                if board[start_row][start_col + i] != EMPTY_CELL:
                    return False
                positions.append((start_row, start_col + i))
        elif direction == 'V':
            if start_row + self.size > BOARD_SIZE:
                return False
            for i in range(self.size):
                if board[start_row + i][start_col] != EMPTY_CELL:
                    return False
                positions.append((start_row + i, start_col))
        else:
            return False

        for pos in positions:
            board[pos[0]][pos[1]] = self.name[0]
        self.positions = positions
        return True

    def hit(self) -> bool:
        self.hits += 1
        return self.hits == self.size

class Destroyer(Ship):
    def __init__(self):
        super().__init__("Destroyer", 2)

class Submarine(Ship):
    def __init__(self):
        super().__init__("Submarine", 3)

class Battleship(Ship):
    def __init__(self):
        super().__init__("Battleship", 4)

class Player:
    def __init__(self, name: str):
        self.name = name
        self.board = [[EMPTY_CELL for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
        self.ships = []
        self.hits = [[EMPTY_CELL for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

    def place_ships(self):
        ships = [Destroyer(), Submarine(), Battleship()]
        for ship in ships:
            while True:
                print(f"{self.name}, coloca tu {ship.name}")
                start_row, start_col, direction = self.get_ship_placement()
                if ship.place_ship(start_row, start_col, direction, self.board):
                    self.ships.append(ship)
                    self.print_board(self.board)
                    break
                else:
                    print("Posición no válida. Inténtalo de nuevo.")

    def get_ship_placement(self) -> tuple:
        while True:
            try:
                start_row = int(input("Fila inicial: "))
                start_col = int(input("Columna inicial: "))
                direction = input("Dirección (H para horizontal, V para vertical): ").upper()
                if 0 <= start_row < BOARD_SIZE and 0 <= start_col < BOARD_SIZE and direction in ['H', 'V']:
                    return start_row, start_col, direction
                else:
                    print("Entrada no válida. Inténtalo de nuevo.")
            except ValueError:
                print("Por favor, ingresa valores válidos.")

    def print_board(self, board: list):
        for row in board:
            print(" ".join(row))
        print()

    def attack(self, opponent: 'Player'):
        while True:
            print(f"{self.name}, elige una posición para atacar.")
            row, col = self.get_attack_position()
            if opponent.board[row][col] == EMPTY_CELL:
                print("Agua!")
                self.hits[row][col] = MISS_CELL
                opponent.board[row][col] = MISS_CELL
                break
            elif opponent.board[row][col] not in [MISS_CELL, HIT_CELL]:
                print("Impacto!")
                self.hits[row][col] = HIT_CELL
                for ship in opponent.ships:
                    if (row, col) in ship.positions:
                        if ship.hit():
                            print(f"¡Hundido! Has hundido el {ship.name}.")
                        break
                opponent.board[row][col] = HIT_CELL
                break
            else:
                print("Ya has atacado esta posición. Intenta de nuevo.")

    def get_attack_position(self) -> tuple:
        while True:
            try:
                row = int(input("Fila: "))
                col = int(input("Columna: "))
                if 0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE:
                    return row, col
                else:
                    print("Posición no válida. Intenta de nuevo.")
            except ValueError:
                print("Por favor, ingresa valores válidos.")

    def all_ships_sunk(self) -> bool:
        return all(ship.hits == ship.size for ship in self.ships)

class BattleshipGame:
    def __init__(self):
        self.player1 = Player("Jugador 1")
        self.player2 = Player("Jugador 2")

    def play(self):
        print("Bienvenido al juego de Batalla Naval!")
        print("Jugador 1 coloca sus barcos.")
        self.player1.place_ships()
        print("Jugador 2 coloca sus barcos.")
        self.player2.place_ships()

        current_player = self.player1
        opponent = self.player2

        while True:
            current_player.attack(opponent)
            if opponent.all_ships_sunk():
                print(f"¡{current_player.name} ha ganado el juego!")
                break
            current_player, opponent = opponent, current_player

if __name__ == "__main__":
    game = BattleshipGame()
    game.play()
