def create_board(size: int) -> list[list[str]]:
    """Создает пустую доску размером size x size"""
    return [["_"] * size for _ in range(size)]

def print_board(board: list[list[str]]):
    """Печатает текущую доску"""
    for row in board:
        print(" ".join(row))
    print()

def make_move(board: list[list[str]], player: str) -> None:
    """Делает ход игрока, спрашивает координаты"""
    size = len(board)
    while True:
        try:
            move = input(f"Игрок {player}, введите строку и столбец через пробел (0-{size-1}): ")
            x_str, y_str = move.split()
            x, y = int(x_str), int(y_str)
            if 0 <= x < size and 0 <= y < size:
                if board[x][y] == "_":
                    board[x][y] = player
                    return
                else:
                    print("Ячейка занята! Попробуйте снова.")
            else:
                print("Координаты вне диапазона! Попробуйте снова.")
        except ValueError:
            print("Ошибка ввода! Введите два числа через пробел.")

def check_winner(board: list[list[str]], win_count: int) -> str | None:
    """Проверяет победителя. Возвращает 'X', '0' или None"""
    size = len(board)
    directions = [(1,0), (0,1), (1,1), (1,-1)]  # вправо, вниз, диагонали

    for i in range(size):
        for j in range(size):
            if board[i][j] == "_":
                continue
            player = board[i][j]
            for dx, dy in directions:
                count = 1
                x, y = i, j
                while True:
                    x += dx
                    y += dy
                    if 0 <= x < size and 0 <= y < size and board[x][y] == player:
                        count += 1
                        if count == win_count:
                            return player
                    else:
                        break
    return None

def is_full(board: list[list[str]]) -> bool:
    """Проверяет, заполнена ли доска"""
    return all(cell != "_" for row in board for cell in row)


# --------------------
# Настройки игры
size = 7          # размер доски
win_count = 4     # сколько символов в ряд для победы

board = create_board(size)
players = ["X", "0"]
current_player_index = 0

print_board(board)

# Игровой цикл
while True:
    make_move(board, players[current_player_index])
    print_board(board)
    
    winner = check_winner(board, win_count)
    if winner:
        print(f"Победитель: {winner}!")
        break
    elif is_full(board):
        print("Ничья!")
        break

    current_player_index = 1 - current_player_index  # смена игрока
8